import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_isUpperCase(target_column,target_table,Execution_Type='',meta={}):
  column = target_column
  dq_rule = 'isUpperCase'
  
  if(Execution_Type == 'Incremental'):
    StrSQl = "SELECT " + target_column + ", CASE WHEN " + target_column + " = upper(" + target_column + ") " \
           "THEN 'PASS' ELSE 'FAIL' END AS DQ_Status FROM " + target_table + " where dqAction = 'NA' "
  else:
    StrSQl = "SELECT " + target_column + ", CASE WHEN " + target_column + " = upper(" + target_column + ") " \
           "THEN 'PASS' ELSE 'FAIL' END AS DQ_Status FROM " + target_table + "  "
  dq_apply_column_data = spark.sql(StrSQl)

  dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
  return dq_report
