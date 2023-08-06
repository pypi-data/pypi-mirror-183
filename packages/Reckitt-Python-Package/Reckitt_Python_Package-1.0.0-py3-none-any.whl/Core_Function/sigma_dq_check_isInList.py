def sigma_dq_check_isInList(target_column,list_of_values,target_table,Execution_Type='',meta={}):
  
  ## convert string to list 
  column = target_column
  dq_rule = 'isInList'
  
  if(Execution_Type == 'Incremental'):
    StrSQl = "select "+target_column+",case when "+target_column+"  in ('"+"','".join(list_of_values)+"') then 'PASS' else 'FAIL' end as DQ_Status from  "+target_table + '                    WHERE dqAction = "NA" '
  else:
    StrSQl = "select "+target_column+",case when "+target_column+" in ('"+"','".join(list_of_values)+"') then 'PASS' else 'FAIL' end as DQ_Status from  "+target_table + ' '
  
  #dq_apply_column_data = spark.sql(StrSQl)

  #dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
  return StrSQl
