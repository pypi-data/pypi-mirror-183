import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_leadingZero(target_column,minimum_zeros, target_table,Execution_Type='',meta = {}):
    leading_zeros = ''
    column = target_column
    dq_rule = 'leadingZero'

    for i in range(minimum_zeros):
        leading_zeros += '0'

    leading_zeros += '%'
    if(Execution_Type == 'Incremental'):
      StrSQl = f"select {column}, case when cast({target_column} as int) is not null " \
              f"and {target_column} like '{leading_zeros}' then 'PASS' else 'FAIL' end as DQ_Status " + \
              f"from {target_table} " + " where dqAction = 'NA' "
    else:
      StrSQl = f"select {column}, case when cast({target_column} as int) is not null " \
              f"and {target_column} like '{leading_zeros}' then 'PASS' else 'FAIL' end as DQ_Status " + \
              f"from {target_table} " + " "
    
    dq_apply_column_data = spark.sql(StrSQl)
    dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
    return dq_report
