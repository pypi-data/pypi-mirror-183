

def sigma_dq_check_isExistingCondAdvanced(target_column, api_response, api_response2, left_join_tables, target_table,
                                          meta={}):

    api_responseSecond = ""
    target_table_for_join = target_table.split('.')
    modified_target_column = target_table + "." + target_column
    modifiedapi_response = ''
    modifiedapi_responseSplit = api_response.split('.')
    andClause = ""
    secondLeftJoin = ""

    StrSQl = ''
    targetTableAPI = target_table_for_join[1]+"."+target_column
    print(modified_target_column)

    modifiedapi_responseSplit
    modifiedORLeftjoin = ''
    if (api_response.__contains__("=")):
        modifiedApiORR_Res = left_join_tables.split('#AND#')

        modifiedApiResForCaseWhen = api_response.replace("=", "==")

        modifiedAPIResponseForEqualTo = api_response.split('=')

        stripmodifiedAPIResponseForEqualTo = []         # stripping
        tableNameInApi_response = []

        for index in modifiedAPIResponseForEqualTo:
            stripmodifiedAPIResponseForEqualTo.append(index.strip())
            tableNameInApi_response.append(index.split(".")[0])

        modifiedAPIResponseForEqualToTemp = modifiedAPIResponseForEqualTo[1].strip()
        index = modifiedAPIResponseForEqualToTemp.index('.')
        modifiedAPIResponseForEqualToTemp = modifiedAPIResponseForEqualToTemp[:index]

        for singleTable in modifiedApiORR_Res:
            index = modifiedApiORR_Res.index(singleTable)
            api_responseSecond = targetTableAPI + " = "+left_join_tables
            api_response_added = api_response + " and " + api_responseSecond
            temp1 = modifiedApiORR_Res[0].split('.')


        if(left_join_tables.split(".")[0] in tableNameInApi_response):
            modifiedORLeftjoin = " left join " + target_table_for_join[0] + "." + temp1[0] + " on " + api_responseSecond
            andClause = " and "+api_response

        else:
            modifiedORLeftjoin = " left join " + target_table_for_join[0] + "." + modifiedAPIResponseForEqualToTemp + " on " + api_response
            secondLeftJoin = " left join "+ target_table_for_join[0] + "."+left_join_tables.split(".")[0]+ " on " + api_responseSecond+" "

        StrSQl = "select " + modified_target_column + ", CASE WHEN " + api_response_added + " \
        THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " + target_table + " \
        " + modifiedORLeftjoin + secondLeftJoin + andClause


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
        StrSQl += " WHERE " + api_response2

    else:
        print("Invalid Input")

    print(StrSQl)




target_table = 'edap_transform.purchase_order'
sigma_dq_check_isExistingCondAdvanced('VENDOR_ACCOUNT_NO','purchase_order.MATERIAL_NO = bill_of_material.SOURCE_ITEM_CODE','entity_classification.supply_Entity_Class = "RB Factory"','entity_classification.supply_Entity',target_table)

#sigma_dq_check_isExistingCondAdvanced('SOURCE_NM','jde_material_master.MATERIAL_NO = production_order.MATERIAL_NO','production_order.SOURCE_NM = "JDE"','jde_material_master.GLOBAL_ITEM_CODE',target_table, 'Incremental')
