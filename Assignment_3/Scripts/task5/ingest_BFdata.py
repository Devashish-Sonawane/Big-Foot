import pandas as pd
import pysolr
import requests
from tqdm.notebook import tqdm

df = pd.read_csv('Data/reports_v3.tsv', sep='\t', encoding='utf8')

json_docs = []
doc_id = 0
target_columns = ['Headline', 'Location Details', 'State', 'County', 'Nearest Town', 'Nearest Road', 'Observed', 'Other Stories',
                  'Environment', 'Follow-Up Report', 'Media Source', 'Source Url', 'Media Issue', 'Observed.1', 'A & G References',
                  'Formatted Address', 'Nearest NP', 'City', 'Image Text', 'Image Caption']
for index, row in tqdm(df.iterrows()):
    json_doc = {}
    tmp_text = ''
    for cn in target_columns:
        tmp_text += str(row[cn])
        tmp_text += ' '
    json_doc["text"] = tmp_text
    json_doc["id"] = str(doc_id)
    doc_id = doc_id + 1
    json_docs.append(json_doc)

core_name = 'bigfoot'
# Create a client instance. The timeout and authentication options are not required.
solr = pysolr.Solr('http://localhost:8983/solr/' + core_name, always_commit=True, timeout=10)

for doc in tqdm(json_docs):
    # How you'd index data.
    solr.add([
        doc
    ])
