import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_isEmail(target_column,target_table,Execution_Type='',meta={}):
    column = target_column
    dq_rule = 'isEmail'

    if(Execution_Type == 'Incremental'):
      StrSQl = "select "+target_column+", CASE WHEN " +target_column+ "  not LIKE '%_@__%.__%' THEN 'FAIL' ELSE 'PASS' END as DQ_Status from " +target_table+ "                   where dqAction = 'NA'  "
    else:
      StrSQl = "select "+target_column+", CASE WHEN " +target_column+ "  not LIKE '%_@__%.__%' THEN 'FAIL' ELSE 'PASS' END as DQ_Status from " +target_table+ "  "



    dq_apply_column_data = spark.sql(StrSQl)
    dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
    return dq_report
