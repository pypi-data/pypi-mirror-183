
def sigma_dq_check_isExistingConditionNew(target_column,api_response,api_response2,left_join_tables,target_table,Execution_Type='',meta={}):
    column = target_column
    dq_rule = 'isExistingConditionNew'
    target_table_for_join = target_table.split('.')
    modified_target_column = target_table + "." + target_column

    print(target_table_for_join)
    print(modified_target_column)

    modifiedapi_response = ''
    modifiedapi_responseSplit = api_response.split('.')

    print(modifiedapi_responseSplit)

    strSQl = ''

    caseWhenCond = ""


    if (api_response.__contains__("=")):
        modified_api_join_table = left_join_tables.split("#AND#")
        print("Inside loop")
        print(modified_api_join_table)

        modifyApiResponseReplaceEqual1 = api_response.replace("=", "==")  # replace = with ==
        print(modifyApiResponseReplaceEqual1)

        modifiedApiResponseSplit = api_response.split("=")         # split across = in api_response
        print(modifiedApiResponseSplit)


        strSQL = "select "+modified_target_column+ ", CASE WHEN "





















# schema  - edap_transform
# target Column - VENDOR_ACCOUNT_NUMBER
# api_response1  - Purchase_order.material_no==Bill_of_Material.source_item_code
# api_response2 - 'Entity_Classification.SUPPLY_ENTITY_CLASS = "RB Factory"#AND#Purchase_order.VENDOR_ACCOUNT_NO==Entity_Classification.SUPPLY_ENTITY'
# api_response3 - 'Bill_of_Material.source_item_code#AND#Entity_Classification.SUPPLY_ENTITY'
# target_table - 'edap_transform.Purchase_order'

target_table = 'edap_transform.production_order'
sigma_dq_check_isExistingConditionNew('SOURCE_NM','jde_material_master.MATERIAL_NO = production_order.MATERIAL_NO','production_order.SOURCE_NM = "JDE"','jde_material_master.GLOBAL_ITEM_CODE',target_table, 'Incremental')

