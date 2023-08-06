import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_fieldCompare_with_value(target_column,api_response,target_table,Execution_Type='',meta={}):
  
  column = target_column
  dq_rule = 'fieldCompare_with_value'


  source_table_with_column = target_table+'.'+target_column
  source_table = target_table

  operator = ''.join(api_response.split('%')[1:-1])
  value = ''.join(api_response.split('%')[::-3])

  try:
      value = float(value)
  except:
      return("Insert valid number")
  else:
      value = float(value)

  if(operator == '>'):#Greater than 0

      operator = '> ' + str(value)
      StrSQl = "select "+source_table_with_column+", CASE WHEN " +source_table_with_column+" "+operator+" THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "

  elif(operator == '>'):#Greater than equal to 0

      operator = '> '+ str(value)
      StrSQl = "select "+source_table_with_column+", CASE WHEN " +source_table_with_column+" "+operator+" THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "

  elif(operator == '<'):#Less than 0

      operator = '< '+ str(value)
      StrSQl = "select "+source_table_with_column+", CASE WHEN " +source_table_with_column+" "+operator+" THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "

  elif(operator == '<='):#Less than equal to 0

      operator = '<= '+ str(value)
      StrSQl = "select "+source_table_with_column+", CASE WHEN " +source_table_with_column+" "+operator+" THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "

  elif(operator == '<>'):#Not equal to 0

      operator = '<> '+ str(value)
      StrSQl = "select "+source_table_with_column+", CASE WHEN " +source_table_with_column+" "+operator+" THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "

  elif(operator == '='):#Not equal to 0

      operator = '= '+ str(value)
      StrSQl = "select "+source_table_with_column+", CASE WHEN " +source_table_with_column+" "+operator+" THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +source_table+"  "


  else:

      return "Error please check the input"

  if(Execution_Type == 'Incremental'): 
      StrSQl += " where dqAction = 'NA'"
    
  dq_apply_column_data = spark.sql(StrSQl)
  
  
  dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
  return dq_report
