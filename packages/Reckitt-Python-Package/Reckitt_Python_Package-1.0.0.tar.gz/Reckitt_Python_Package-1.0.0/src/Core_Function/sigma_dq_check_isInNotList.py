import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_isInNotList(target_column,list_of_values,Execution_Type='',meta={}):
  
  ## convert string to list 
  column = target_column
  dq_rule = 'isInNotList'
  
  if(Execution_Type == 'Incremental'):
    StrSQl = "select "+target_column+",case when "+target_column+" not in ('"+"','".join(list_of_values)+"') then 'PASS' else 'FAIL' end as DQ_Status from  "+target_table + ' WHERE dqAction = "NA" '
  else:
    StrSQl = "select "+target_column+",case when "+target_column+" not in ('"+"','".join(list_of_values)+"') then 'PASS' else 'FAIL' end as DQ_Status from  "+target_table + ' '
  
  dq_apply_column_data = spark.sql(StrSQl)

  dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
  return dq_report
