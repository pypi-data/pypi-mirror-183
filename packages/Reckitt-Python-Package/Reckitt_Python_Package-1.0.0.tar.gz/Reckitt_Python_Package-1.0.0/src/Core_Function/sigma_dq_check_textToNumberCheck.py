import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_textToNumberCheck(target_column,target_table,Execution_Type='',meta={}):
    column = target_column
    dq_rule = 'textToNumberCheck'


    if(Execution_Type == 'Incremental'): 
      StrSQl = f"select {target_column}, case when cast(replace(replace({target_column}, ',', ''), ' ', ') as INT) > 0" \
              f" and {target_column}%1 == 0 then 'PASS' else 'FAIL' end as DQ_Status from {target_table}" \
              f" where dqAction = 'NA'   "
    else:
      StrSQl = f"select {target_column}, case when cast(replace(replace({target_column}, ',', ''), ' ', ') as INT) > 0" \
              f" and {target_column}%1 == 0 then 'PASS' else 'FAIL' end as DQ_Status from {target_table}" \
              f"   "
      
    dq_apply_column_data = spark.sql(StrSQl)
    dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
    return dq_report
