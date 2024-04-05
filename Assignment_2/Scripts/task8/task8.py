import pandas as pd
import spacy
import time
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")
beam_width = 16
beam_density = 0.0001
file_path = r"Dataset1\reports_v2_task7.tsv"

df = pd.read_csv(file_path, sep ="\t")

def extract_unique_entities(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = set()
        entities[ent.label_].add(ent.text)
    return entities

def calculate_entity_scores(text):
    doc = nlp(text)
    entity_scores = defaultdict(float)
    total_entities = len(doc.ents)  
    if total_entities > 0:
        for ent in doc.ents:
            entity_scores[(ent.start_char, ent.end_char, ent.label_)] += 1 / total_entities  
    return entity_scores

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    unique_entities_row = {}
    entity_scores_row = defaultdict(float)
    
    # Iterate over each column in the row
    for column_name, column_value in row.items():
        # Extract unique entities and calculate scores for the column value
        unique_entities_column = extract_unique_entities(str(column_value))
        entity_scores_column = calculate_entity_scores(str(column_value))
        
        # Merge unique entities and scores from the column into the row's dictionaries
        for entity_type, values in unique_entities_column.items():
            if entity_type not in unique_entities_row:
                unique_entities_row[entity_type] = set()
            unique_entities_row[entity_type].update(values)
        
        for (start, end, label), score in entity_scores_column.items():
            entity_scores_row[(start, end, label)] += score
    
    # Add extracted entities and scores as new columns to the DataFrame
    for entity_type, values in unique_entities_row.items():
        df.at[index, f"{entity_type}_entities"] = ', '.join(values)
    
    for (start, end, label), score in entity_scores_row.items():
        df.at[index, f"{label}_score"] = score
        
    print(f"Finished row {index} at {time.strftime("%H:%M:%S", time.localtime())}")

# Save the modified DataFrame
df.to_csv(r"Dataset1\reports_v2_task8.tsv", sep="\t", index=False)
