import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_isDate(target_column,api_response,target_table,Execution_Type='',meta={}):
    column = target_column
    dq_rule = 'isDate'

    if api_response == 'dd.mm.YY' or api_response == 'dd/mm/YY' or api_response == 'dd-mm-YY':

      StrSQl = "select "+target_column+", CASE WHEN " +target_column+" REGEXP '^([0]?[1-9]|[1|2][0-9]|[3][0|1])[.\/-]([0]?[1-9]|[1][0-2])[.\/-]([0-9]{4}|[0-9]{2})$' THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+ "  "

    elif api_response == 'mm.dd.YY' or api_response == 'mm/dd/YY' or api_response == 'mm-dd-YY':

      StrSQl = "select "+target_column+", CASE WHEN " +target_column+" REGEXP '^([0]?[1-9]|[1][0-2])[.\/-]([0]?[1-9]|[1|2][0-9]|[3][0|1])[.\/-]([0-9]{4}|[0-9]{2})$' THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+ " "

    elif api_response == 'YY.mm.dd' or api_response == 'YY/mm/dd' or api_response == 'YY-mm-dd':

      StrSQl = "select "+target_column+", CASE WHEN " +target_column+" REGEXP '^([0-9]{4}|[0-9]{2})[.\/-]([0]?[1-9]|[1][0-2])[.\/-]([0]?[1-9]|[1|2][0-9]|[3][0|1])$' THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+ "  "

    elif api_response == 'YYmmdd':

      StrSQl = "select "+target_column+", CASE WHEN " +target_column+" REGEXP '^([0-9]{4}|[0-9]{2})([0]?[1-9]|[1][0-2])([0]?[1-9]|[1|2][0-9]|[3][0|1])$' THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+ "  "

    elif api_response == 'ddmmYY':

      StrSQl = "select "+target_column+", CASE WHEN " +target_column+" REGEXP '^([0]?[1-9]|[1|2][0-9]|[3][0|1])([0]?[1-9]|[1][0-2])([0-9]{4}|[0-9]{2})$' THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+ "  "

    elif api_response == 'mmddYY':

      StrSQl = "select "+target_column+", CASE WHEN " +target_column+" REGEXP '^([0]?[1-9]|[1][0-2])([0]?[1-9]|[1|2][0-9]|[3][0|1])([0-9]{4}|[0-9]{2})$' THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+ "  "


    else:

      print('Incorrect/Unsupported Format Selected')

    if(Execution_Type == 'Incremental'): 
       StrSQl += " where dqAction = 'NA'"
    dq_apply_column_data = spark.sql(StrSQl)
    dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
    return dq_report
