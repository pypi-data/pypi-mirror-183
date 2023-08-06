import requests


def sigma_dq_helper_get_pipeline_table_id(url,target_table):
  
  pipeline_table_id_path = 'v1/table/get_table_id/{}'.format(target_table)
  pipeline_table_id_url = url + pipeline_table_id_path
  api_call_ = requests.get(pipeline_table_id_url)
  pipeline_table_id = api_call_.json()['id']
  return pipeline_table_id
