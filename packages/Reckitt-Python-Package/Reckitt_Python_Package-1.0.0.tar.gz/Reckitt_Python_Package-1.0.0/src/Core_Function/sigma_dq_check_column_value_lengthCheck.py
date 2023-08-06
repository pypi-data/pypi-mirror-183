import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_column_value_lengthCheck(target_column,api_response,Execution_Type=''):
    column = target_column
    dq_rule = 'islengthCheck'
    api_response = api_response.split('#AND#')
     
    if(Execution_Type == 'Incremental'):  
        StrSQl = "select "+target_column+", CASE WHEN LENGTH("+target_column+") > "+api_response[0]+" AND LENGTH("+target_column+") < "+api_response[1]+" THEN                       'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table +" where dqAction = 'NA' "
    else:
        StrSQl = "select "+target_column+", CASE WHEN LENGTH("+target_column+") > "+api_response[0]+" AND LENGTH("+target_column+") < "+api_response[1]+" THEN                       'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table
    
    dq_apply_column_data = spark.sql(StrSQl)
   
    dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
    return dq_report
