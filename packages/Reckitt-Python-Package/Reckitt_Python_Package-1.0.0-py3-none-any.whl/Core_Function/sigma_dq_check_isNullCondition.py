def sigma_dq_check_isNullCondition(target_column: str, api_response: str,target_table: str,Execution_Type='',meta={}):

  conditions = api_response.split('#and#')
  case_list = []
  column = target_column
  dq_rule = 'isNullCondition'
  for condition in conditions:
      case = ""
      if condition.__contains__("="):
          case = condition.replace("=", "==")
      elif condition.__contains__("is null"):
          case = condition  # TODO
      elif condition.__contains__("is not null"):
          case = condition  # TODO
      elif condition.__contains__("not like"):
          clause = condition.split("not like")
          pattern = clause[1].strip().replace("'", "").replace('"', '')
          case = f"{clause[0].strip()} not like '%{pattern}%'"
      elif condition.__contains__("like"):
          clause = condition.split("like")
          pattern = clause[1].strip().replace("'", "").replace('"', '')
          case = f"{clause[0].strip()} like '%{pattern}%'"
      elif condition.__contains__("not in"):
          case = condition  # TODO
      elif condition.__contains__("in"):
          case = condition  # TODO
      case_list.append(case)

  sql_case_when = ""
  common_condition = f"({target_column} is null or trim({target_column}) == '') then 'FAIL'"
  if len(case_list) > 0:
      for case in case_list:
          if case_list.index(case) == 0:
              sql_case_when += " case"
          sql_case_when += f" when {case} and {common_condition}"
  else:
      sql_case_when = f" case when {common_condition}"

  sql_case_when += f" else 'PASS' end as DQ_Status"

  if(Execution_Type == 'Incremental'):
     StrSQl = f"select {target_column},{sql_case_when} from {target_table}  where dqAction = 'NA'"
  else:
     StrSQl = f"select {target_column},{sql_case_when} from {target_table} "

  dq_apply_column_data = spark.sql(StrSQl)

  dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
  return dq_report