import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_isInListCond(target_column,list_of_values,api_response,target_table,Execution_Type='',meta={}):
  column = target_column
  dq_rule = 'isInListCond'
  
  database_name = target_table.split('.')[0]
      
  StrSQl = "Select " + target_column + ", case when " + target_column + " in ('" +"','".join(list_of_values) + "') then 'PASS' else 'FAIL' end as DQ_Status from " + target_table + " "
  
  if(api_response != ''):
      lsmodifiedApliResponse = ''
      if(not api_response.__contains__("#AND#") and api_response.__contains__("%OR%")):
          lsmodifiedApliResponse = database_name+"."+api_response.replace("%OR%", " OR "+database_name+".")
      elif(not api_response.__contains__("%OR%") and api_response.__contains__("#AND#")):
         lsmodifiedApliResponse =database_name+"."+api_response.replace("#AND#", " AND "+database_name+".")
      elif(api_response.__contains__("%OR%") and api_response.__contains__("#AND#")):
         lsmodifiedApliResponse  = database_name+"."+api_response.replace("#AND#", "AND "+database_name+".").replace("%OR%", " OR "+database_name+".")
      else:
          lsmodifiedApliResponse = database_name+"."+api_response
          
      StrSQl += " WHERE " +lsmodifiedApliResponse
      
      if(Execution_Type == 'Incremental'):
        StrSQl += " and dqAction = 'NA'"
      
  dq_apply_column_data = spark.sql(StrSQl)
  dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
  return dq_report
