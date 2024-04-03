# Import necessary libraries
import pandas as pd
import pysolr
import requests

# Load a dataset from the assignment 2 output TSV file
df = pd.read_csv('Data/reports_v3.tsv', sep='\t', encoding='utf8')

# Initialize an empty list to store JSON documents and a document ID counter
json_docs = []
doc_id = 0

# Define the columns from the dataset that will be included in the JSON documents
target_columns = ['Headline', 'Location Details', 'State', 'County', 'Nearest Town', 'Nearest Road', 'Observed', 'Other Stories',
                  'Environment', 'Follow-Up Report', 'Media Source', 'Source Url', 'Media Issue', 'Observed.1', 'A & G References',
                  'Formatted Address', 'Nearest NP', 'City', 'Image Text', 'Image Caption']

# Loop over each row in the DataFrame to create a JSON document
for index, row in df.iterrows():
    # Initialize an empty dictionary for the current JSON document
    json_doc = {}
    # Initialize an empty string to concatenate the text from target columns
    tmp_text = ''
    # Loop over each target column
    for cn in target_columns:
        # Append the text from the current column to the temporary text string
        tmp_text += str(row[cn])
        tmp_text += ' '
    # Assign the concatenated text to the "text" field of the JSON document
    json_doc["text"] = tmp_text
    # Assign a unique ID to the "id" field of the JSON document
    json_doc["id"] = str(doc_id)
    # Increment the document ID counter
    doc_id = doc_id + 1
    # Add the JSON document to the list of documents
    json_docs.append(json_doc)

# Specify the Solr core name
core_name = 'bigfoot'
# Create a Solr client instance with the specified core name
solr = pysolr.Solr('http://localhost:8983/solr/' + core_name, always_commit=True, timeout=10)

# Get the number of documents
n_doc = len(json_docs)
# Initialize a counter for indexing progress
i = 1
for doc in json_docs:
    # Print the current progress of indexing
    print("\r" + str(i) + "/" + str(n_doc), end="")
    # Index the current document in Solr
    solr.add([
        doc
    ])
    # Increment the progress counter
    i += 1
