import pandas as pd
import json

def extract_and_filter_entities(file_path, min_count=50, output_json_file='BFRO_vis_3.json'):
    
    full_detected_objects = pd.read_csv(file_path, sep='\t', usecols=['Detected Objects'])
    
    entities = full_detected_objects['Detected Objects'].str.split(', ').explode()
    
    entity_counts = entities.value_counts()
    
    filtered_entities = entity_counts[entity_counts > min_count]
    
    entities_dict = filtered_entities.to_dict()
    
    with open(output_json_file, 'w') as json_file:
        json.dump(entities_dict, json_file, indent=4)
    
    return entities_dict

entities_counts = extract_and_filter_entities(file_path='Data/reports_v3.tsv', min_count=50)
