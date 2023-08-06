import spark

from src.Core_Function.sigma_dq_check_isExistingCond import target_table
from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_customPatternCheck(target_column,api_response,Execution_Type=''):
    column = target_column
    dq_rule = 'sigma_dq_check_expect_column_values_to_match_regex'
    
    if(Execution_Type == 'Incremental'):
      StrSQl = "select "+target_column+", CASE WHEN " +target_column+" REGEXP '"+api_response+"' THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+"                   where dqAction = 'NA'"
    else:
      StrSQl = "select "+target_column+", CASE WHEN " +target_column+" REGEXP '"+api_response+"' THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table                
      
    dq_apply_column_data = spark.sql(StrSQl)
   
    dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
    return dq_report

