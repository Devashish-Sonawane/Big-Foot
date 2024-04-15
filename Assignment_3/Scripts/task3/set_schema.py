import pandas as pd
import requests
import json

# Load the TSV file made in assingment 2.
df = pd.read_csv('../../Data/reports_v3.tsv', sep='\t', encoding='utf8')

# Prefix all column names in the DataFrame with 'BF_' to avoid naming conflicts with existing Solr schema fields.
df = df.add_prefix('BF_')

# Replace spaces and '&' in column names with underscores to match the formatting requirements for Solr schema fields.
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('&', '_')

# Define the base URL and core name for Solr.
solr_url = 'http://localhost:8983/solr'
core_name = 'bigfoot'

# Function to create a field definition based on the column name and data type.
def create_field_definition(column_name, dtype):
    field_type = 'string'
    # Assign Solr field types based on pandas data types.
    if pd.api.types.is_integer_dtype(dtype):
        field_type = 'pint'
    elif pd.api.types.is_float_dtype(dtype):
        field_type = 'pfloat'
    elif pd.api.types.is_datetime64_dtype(dtype):
        field_type = 'pdate'
    elif column_name in ['BF_Observed.1']:
        field_type = 'text_general'  # Special case for text fields
    # Return the field definition as a dictionary.
    return {
        'add-field': {
            'name': column_name,
            'type': field_type,
            'indexed': True,
            'stored': True
        }
    }

# Function to add a field to Solr schema using HTTP POST.
def add_field_to_solr(field_definition):
    url = f'{solr_url}/{core_name}/schema'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, json=field_definition, headers=headers)
    return response

# Loop through each column in DataFrame, create a field definition, and add it to Solr.
for column in df.columns:
    field_def = create_field_definition(column, df[column].dtype)
    response = add_field_to_solr(field_def)
    if response.status_code == 200:
        print(f"Field '{column}' added successfully.")
    else:
        print(f"Error adding field '{column}': {response.json()}")

# Save the modified DataFrame as a JSON file to ingest later steps.
with open('../../Dataset1/BFRO_task3.json', 'w') as f:
    json.dump(df.to_dict(orient='records'), f, indent=2)
