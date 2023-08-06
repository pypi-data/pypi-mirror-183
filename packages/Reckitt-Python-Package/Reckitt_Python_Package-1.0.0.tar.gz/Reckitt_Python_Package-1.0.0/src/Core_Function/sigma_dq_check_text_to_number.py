import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_text_to_number(target_column, target_table, Execution_Type='', meta = {}, column=None, dq_rule=None):

  
  if(Execution_Type == 'Incremental'):
    StrSQl = f"select {target_column}, case when cast(replace(replace({target_column}, ',', ''), ' ', '') " \
            f"as INT) is not null and cast(replace(replace({target_column}, ',', ''), ' ', '') as FLOAT)%1 == 0 " \
            f"then 'PASS' else 'FAIL' end as DQ_Status from {target_table}  where dqAction = 'NA'"
  else:
    StrSQl = f"select {target_column}, case when cast(replace(replace({target_column}, ',', ''), ' ', '') " \
            f"as INT) is not null and cast(replace(replace({target_column}, ',', ''), ' ', '') as FLOAT)%1 == 0 " \
            f"then 'PASS' else 'FAIL' end as DQ_Status from {target_table} "
  
  dq_apply_column_data = spark.sql(StrSQl)

  dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
  return dq_report
