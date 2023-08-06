def sigma_dq_check_isExistingCond(target_column,api_response,api_response2,target_table,Execution_Type='',meta={}):
    column = target_column
    dq_rule = 'isExistingCond'
    target_table_for_join = target_table.split('.')
    modified_target_column = target_table+"."+target_column

    print(target_table_for_join)
    print(modified_target_column)

    modifiedapi_response =''
    modifiedapi_responseSplit = api_response.split('.')

    print(modifiedapi_responseSplit)
    modifiedapi_leftJoinresponse2 = ''
    StrSQl = ''
    if(api_response.__contains__("%OR%")):
        modifiedApiOR_Res = api_response.split('%OR%')
        modifiedORFinal=''
        modifiedORLeftjoin = ''
        left_join_singleTable = ''
        #print(len(modifiedApiOR_Res))
        for singleTable in modifiedApiOR_Res:
            left_join_singleTable = singleTable.split('.') 
            index = modifiedApiOR_Res.index(singleTable)
            if(index >= 1):
                modifiedORFinal += " OR "+modified_target_column +" == " +singleTable #operator goes here
                modifiedORLeftjoin += " left join "+target_table_for_join[0]+"."+left_join_singleTable[0]+" on "+modified_target_column +" = " +singleTable  #Appendlogicneedstobe impleted
            else:
                modifiedORFinal += modified_target_column +" == " +singleTable   #operator goes here
                modifiedORLeftjoin = " left join "+target_table_for_join[0]+"."+left_join_singleTable[0]+" on "+modified_target_column +" = " +singleTable       
        
        StrSQl = "select "+modified_target_column+", CASE WHEN " +modifiedORFinal+" \
                THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+" \
                " +modifiedORLeftjoin
    
    elif(api_response.__contains__("#AND#")):
        modifiedApiAND_Res = api_response.split('#AND#')
        modifiedANDFinal=''
        modifiedANDLeftjoin = ''
        left_join_singleTable = ''
        for singleTable in modifiedApiAND_Res:
            left_join_singleTable = singleTable.split('.') 
            index = modifiedApiAND_Res.index(singleTable)
            if(index >= 1):
                modifiedANDFinal += " AND "+modified_target_column +" == " +singleTable #operator goes here
                modifiedANDLeftjoin += " left join "+target_table_for_join[0]+"."+left_join_singleTable[0]+" on "+modified_target_column +" = " +singleTable  #Appendlogicneedstobe impleted
            else:
                modifiedANDFinal += modified_target_column +" == " +singleTable  #operator goes here
                modifiedANDLeftjoin = " left join "+target_table_for_join[0]+"."+left_join_singleTable[0]+" on "+modified_target_column +" = " +singleTable
        
        StrSQl = "select "+modified_target_column+", CASE WHEN " +modifiedANDFinal+" \
            THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+" \
            " +modifiedANDLeftjoin
        
    else: # When my api_response    = 'JDE_VENDOR.global_vendor_number
        modifiedapi_response += modified_target_column +" == " +api_response   #operator goes here
        modifiedORLeftjoin = " left join "+target_table_for_join[0]+"."+modifiedapi_responseSplit[0]+" on "+modified_target_column +" = " +api_response       
        StrSQl = "select "+modified_target_column+", CASE WHEN " +modifiedapi_response+" \
                THEN 'PASS' ELSE 'FAIL' END as DQ_Status from " +target_table+" \
                " +modifiedORLeftjoin
 
    if(api_response2 != ''):
        lsmodifiedApliResponse = ''
        if(not api_response2.__contains__("#AND#") and api_response2.__contains__("%OR%")):
            lsmodifiedApliResponse = target_table_for_join[0]+"."+api_response2.replace("%OR%", " OR "+target_table_for_join[0]+".")
        elif(not api_response2.__contains__("%OR%") and api_response2.__contains__("#AND#")):
           lsmodifiedApliResponse =target_table_for_join[0]+"."+api_response2.replace("#AND#", " AND "+target_table_for_join[0]+".")
        elif(api_response2.__contains__("%OR%") and api_response2.__contains__("#AND#")):
           lsmodifiedApliResponse  = target_table_for_join[0]+"."+api_response2.replace("#AND#", "AND "+target_table_for_join[0]+".").replace("%OR%", " OR "+target_table_for_join[0]+".")
        else:
            lsmodifiedApliResponse = target_table_for_join[0]+"."+api_response2
        StrSQl += " WHERE " +lsmodifiedApliResponse

        if(Execution_Type == 'Incremental'):
            StrSQl += " and "+target_table+"."+"dqAction = 'NA'"
    else:
      print("Invalid Input")

    
    #print(StrSQl)
    #dq_apply_column_data = spark.sql(StrSQl)
    
    #dq_report = sigma_dq_generate_dq_report(dq_apply_column_data,column,dq_rule)
  
    #return dq_report

target_table = 'edap_transform.Purchase_order'

sigma_dq_check_isExistingCond('MATERIAL_NO','JDE_Material_Master.Global_item_code ','Purchase_order.SOURCE_NM= "JDE"',target_table)
