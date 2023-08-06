import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_fieldCompare_with_current_date(target_column,api_response,target_table,Execution_Type='',meta={}):
    column = target_column
    dq_rule = 'fieldCompare_with_current_date'


    source_table_with_column = target_table+'.'+target_column
    source_table = target_table
    
    
    if(api_response == '< current_date'):#Less than Current date

        operator = ' < '
        StrSQl = "select "+source_table_with_column+", CASE WHEN to_date(" +source_table_with_column+", 'yyyy-MM-dd') "+operator+" current_date() THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "

    elif(api_response == '> current_date'):#Greater than Current date

        operator = ' > '
        StrSQl = "select "+source_table_with_column+", CASE WHEN to_date(" +source_table_with_column+", 'yyyy-MM-dd') "+operator+" current_date() THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "
    
    elif(api_response == '<= current_date'):#Greater than Current date

        operator = ' <= '
        StrSQl = "select "+source_table_with_column+", CASE WHEN to_date(" +source_table_with_column+", 'yyyy-MM-dd') "+operator+" current_date() THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "
    
    elif(api_response == '>= current_date'):#Greater than Current date

        operator = ' >= '
        StrSQl = "select "+source_table_with_column+", CASE WHEN to_date(" +source_table_with_column+", 'yyyy-MM-dd') "+operator+" current_date() THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "
    
    elif(api_response == '= current_date'):#Greater than Current date

        operator = ' = '
        StrSQl = "select "+source_table_with_column+", CASE WHEN to_date(" +source_table_with_column+", 'yyyy-MM-dd') "+operator+" current_date() THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "
    
    elif(api_response == '<> current_date'):#Greater than Current date

        operator = ' != '
        StrSQl = "select "+source_table_with_column+", CASE WHEN to_date(" +source_table_with_column+", 'yyyy-MM-dd') "+operator+" current_date() THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "
    
    else:

        return "Error please check the input"

    if(Execution_Type == 'Incremental'): 
        StrSQl += " where dqAction = 'NA'"
    dq_apply_column_data = spark.sql(StrSQl)


    dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
    return dq_report
