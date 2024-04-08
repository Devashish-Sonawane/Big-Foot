# This is a sample code for task 1, please modify and use it as needed.

# Import necessary libraries
import pandas as pd
import json

# Load a dataset from the assignment 2 output TSV file
df = pd.read_csv('Data/reports_v3.tsv', sep='\t', encoding='utf8')

# Convert DataFrame to a dictionary of records and wrap in another dictionary
dic = {'BFRO': df.to_dict(orient='records')}

# Write the dictionary to a JSON file with pretty printing
with open('Dataset1/BFRO.json', 'w') as f:
    json.dump(dic, f, indent=2)
