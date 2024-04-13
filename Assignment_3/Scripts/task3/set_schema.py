import pandas as pd
import requests
import json

df = pd.read_csv('../../Data/reports_v3.tsv', sep='\t', encoding='utf8')
df = df.add_prefix('BF_')
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('&', '_')

solr_url = 'http://localhost:8983/solr'
core_name = 'bigfoot'

def create_field_definition(column_name, dtype):
    field_type = 'string'
    if pd.api.types.is_integer_dtype(dtype):
        field_type = 'pint'
    elif pd.api.types.is_float_dtype(dtype):
        field_type = 'pfloat'
    elif pd.api.types.is_datetime64_dtype(dtype):
        field_type = 'pdate'
    elif column_name in ['BF_Observed.1']:
        field_type = 'text_general'

    return {
        'add-field': {
            'name': column_name,
            'type': field_type,
            'indexed': True,
            'stored': True
        }
    }

def add_field_to_solr(field_definition):
    url = f'{solr_url}/{core_name}/schema'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, json=field_definition, headers=headers)
    return response

for column in df.columns:
    field_def = create_field_definition(column, df[column].dtype)
    response = add_field_to_solr(field_def)
    if response.status_code == 200:
        print(f"Field '{column}' added successfully.")
    else:
        print(f"Error adding field '{column}': {response.json()}")

with open('../../Dataset1/BFRO_task3.json', 'w') as f:
    json.dump(df.to_dict(orient='records'), f, indent=2)
