import spark

from src.Helper_Function.sigma_dq_generate_dq_report import sigma_dq_generate_dq_report


def sigma_dq_check_isExistingCondAdvanced(target_column, api_response, api_response2, left_join_tables, target_table,
                                          Execution_Type='', meta={}):
    target_table_for_join = target_table.split('.')
    column = target_column
    modified_target_column = target_table + "." + target_column
    modifiedapi_response = ''
    modifiedapi_responseSplit = api_response.split('.')
    modifiedapi_leftJoinresponse2 = ''
    StrSQl = ''
    dq_rule = 'isExistingCondAdvanced'
    modifiedapi_responseSplit

    if (api_response.__contains__("=")):
        modifiedApiORR_Res = left_join_tables.split('#AND#')
        modifiedApiResForCaseWhen = api_response.replace("=", "==")
        modifiedAPIResponseForEqualTo = api_response.split('=')
        for i in modifiedAPIResponseForEqualTo:
            modified_i = i.split('.')
            leftjointable = modified_i[0].strip()
            leftjointable_temp = target_table_for_join[1].strip()
            if leftjointable != leftjointable_temp:
                modifiedAPIResponseForEqualToTemp = target_table_for_join[0] + "." + modified_i[0]
                modifiedAPIResponseForEqualToTemp1 = modifiedAPIResponseForEqualToTemp
        index = modifiedAPIResponseForEqualToTemp.index('.')
        modifiedAPIResponseForEqualToTemp = modifiedAPIResponseForEqualToTemp[:index]
        modifiedORLeftjoin = ''
        left_join_singleTable = ''
        modifiedApiORR_Res_len = len(modifiedApiORR_Res)
        for singleTable in modifiedApiORR_Res:
            index = modifiedApiORR_Res.index(singleTable)
            if (index >= 1):
                tempsingleTable = singleTable
                temp = singleTable.split('.')
                modifiedORLeftjoin += " left join " + target_table_for_join[0] + "." + temp[
                    0] + " on " + modified_target_column + " = " + tempsingleTable  # Appendlogicneedstobe impleted
            else:
                temp1 = modifiedApiORR_Res[0].split('.')
                modifiedORLeftjoin = " left join " + target_table_for_join[0] + "." + temp1[0] + " on " + \
                                     target_table_for_join[0] + "." + modifiedAPIResponseForEqualTo[
                                         0] + " = " + singleTable

        StrSQl = "select " + modified_target_column + ", CASE WHEN " + target_table_for_join[
            0] + "." + modifiedApiResForCaseWhen + " \
                THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " + target_table + " \
                " + modifiedORLeftjoin
        if (not modifiedORLeftjoin.__contains__(modifiedAPIResponseForEqualToTemp1)):
            StrSQl += " left join " + modifiedAPIResponseForEqualToTemp1 + " ON " + api_response


    else:  # When my api_response    = 'JDE_VENDOR.global_vendor_number
        temp1 = left_join_tables.split('.')
        modifiedapi_response += modified_target_column + " == " + api_response  # operator goes here
        modifiedORLeftjoin = " left join " + target_table_for_join[0] + "." + modifiedapi_responseSplit[
            0] + " on " + modified_target_column + " = " + api_response
        modifiedORLeftjoin += " left join " + target_table_for_join[0] + "." + temp1[0]
        StrSQl = "select " + modified_target_column + ", CASE WHEN " + modifiedapi_response + " \
                THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " + target_table + " \
                " + modifiedORLeftjoin

    if (api_response2 != ''):
        lsmodifiedApliResponse = ''
        if (not api_response2.__contains__("#AND#") and api_response2.__contains__("%OR%")):
            lsmodifiedApliResponse = target_table_for_join[0] + "." + api_response2.replace("%OR%", " OR " +
                                                                                            target_table_for_join[
                                                                                                0] + ".")
        elif (not api_response2.__contains__("%OR%") and api_response2.__contains__("#AND#")):
            lsmodifiedApliResponse = target_table_for_join[0] + "." + api_response2.replace("#AND#", " AND " +
                                                                                            target_table_for_join[
                                                                                                0] + ".")
        elif (api_response2.__contains__("%OR%") and api_response2.__contains__("#AND#")):
            lsmodifiedApliResponse = target_table_for_join[0] + "." + api_response2.replace("#AND#", "AND " +
                                                                                            target_table_for_join[
                                                                                                0] + ".").replace(
                "%OR%", " OR " + target_table_for_join[0] + ".")
        else:
            lsmodifiedApliResponse = target_table_for_join[0] + "." + api_response2
        StrSQl += " WHERE " + lsmodifiedApliResponse

    if (Execution_Type == 'Incremental'):
        StrSQl += " and " + target_table + ".UPDATE_RUN_TS = (select MAX(UPDATE_RUN_TS) from " + target_table + ") OR " + target_table + ".dqAction = 'NA'"


    else:
        print("Invalid Input")

    print(StrSQl)
    dq_apply_column_data = spark.sql(StrSQl)

    dq_report = sigma_dq_generate_dq_report(dq_apply_column_data, column, dq_rule)

    return dq_report

