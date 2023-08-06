import spark

from src.Helper_Function.sigma_dq_helper_generate_dq_action import sigma_dq_helper_generate_dq_action
from src.Helper_Function.sigma_dq_helper_generate_dq_message import sigma_dq_helper_generate_dq_message


def sigma_dq_check_isDuplicate(list_of_columns,target_table,Execution_Type = '',meta={}):
  dq_rule = 'isDuplicate'
  
  columns = ','.join(list_of_columns)
  column = columns
 
  
  if(Execution_Type == 'Incremental'):
      StrSQl = f"select {columns}, count(1), case when count(1) > 1 then 'FAIL' else 'PASS' end as DQ_Status from " \
            f"{target_table} where dqAction = 'NA' group by {columns} ORDER BY {len(list_of_columns) + 1} DESC "
  else:
      StrSQl = f"select {columns}, count(1), case when count(1) > 1 then 'FAIL' else 'PASS' end as DQ_Status from " \
            f"{target_table} group by {columns} ORDER BY {len(list_of_columns) + 1} DESC "
  
  dq_apply_column_data = spark.sql(StrSQl)
  
  ## additional handling required for list of columns as main argument
  failed_values_dict = {}

  
  
  dq_report = {}
  dq_report['column'] = columns
  dq_report['rule'] = dq_rule
  dq_report['total_rows_checked'] = dq_apply_column_data.count()
  total_DQ_Pass_count = dq_apply_column_data.filter(dq_apply_column_data.DQ_Status == 'PASS').count()
  dq_report['total_rows_failed'] = dq_apply_column_data.filter(dq_apply_column_data.DQ_Status == 'FAIL').count()
  if dq_report['total_rows_failed'] > 0:
    dq_report['success'] = False
    dq_report['failed_percent'] = (dq_report['total_rows_failed']/dq_report['total_rows_checked'])*100
    raw_fail_list = dq_apply_column_data.select([c for c in dq_apply_column_data.columns if c in list_of_columns]
                                                              ).filter(dq_apply_column_data.DQ_Status == 'FAIL'
                                                                      ).rdd.flatMap(lambda x: x).collect()
    dq_apply_column_data_ = dq_apply_column_data.filter(dq_apply_column_data.DQ_Status == 'FAIL').toPandas()
    failed_values_dict = dq_apply_column_data_.to_dict(orient='list')
    for i in dq_apply_column_data.columns:
      if i not in list_of_columns:
        del failed_values_dict[i]
        
    raw_fail_list_ = failed_values_dict     
    #raw_fail_list_ = sigma_dq_helper_unique_elements_in_list(raw_fail_list)
    dq_report['failed_values'] = raw_fail_list_
  elif dq_report['total_rows_failed'] == dq_report['total_rows_checked']:
    dq_report['success'] = False
    dq_report['failed_percent'] = (dq_report['total_rows_failed']/dq_report['total_rows_checked'])*100
    dq_report['failed_values'] = []
  else:
    dq_report['success'] = True
    dq_report['passed_percent'] = (total_DQ_Pass_count/dq_report['total_rows_checked'])*100



  dq_report['meta'] = meta
  dq_report_parent ={}
  dq_report_parent[0]= dq_report
  
  dq_message = sigma_dq_helper_generate_dq_message(dq_report_parent)
  dq_action = sigma_dq_helper_generate_dq_action(dq_message)
  
  dq_apply_column_data.createOrReplaceTempView('results_out')
  
  COALESCE_target = ' '
  COALESCE_results_out = ' '

  for cols in list_of_columns:
      COALESCE_target += f"COALESCE({target_table}.{cols}, '') ,"

  COALESCE_target = COALESCE_target[:-1]

  for cols in list_of_columns:
      COALESCE_results_out += f"COALESCE(results_out.{cols}, '') ,"

  COALESCE_results_out = COALESCE_results_out[:-1]
  
  StrSQl_update = f"merge into  {target_table} using results_out on CONCAT({COALESCE_target}) = CONCAT({COALESCE_results_out}) WHEN MATCHED and results_out.DQ_Status = 'FAIL' THEN UPDATE SET dqAction = '{dq_action}', dqMessage = Concat(dqMessage, ' ,{dq_message[0]['column_name']} for rule {dq_message[0]['rule']} failed , ')"
  
  try:
    spark.sql(StrSQl_update)
    status_ = "Writing DQ_Action and DQ_Message into " + target_table +" completed "
  except Exception as e:
    status_ = "Writing DQ_Action and DQ_Message into " + target_table +" failed\n" + str(e) 
    #return status_
  
  
  print(status_)
  return dq_report
