import pandas as pd
import json

def process_entities(file_path: str, min_count: int = 50, output_json_file: str = 'BFRO_vis_3.json') -> list:
    """Extracts, filters, categorizes, and formats entities from a TSV file.

    Args:
        file_path (str): Path to the TSV file.
        min_count (int): Minimum count threshold to include an entity.
        output_json_file (str): Path for the output JSON containing categorized entities.

    Returns:
        list: List of dictionaries with each entity's name, count, and category.
    """
    # Configuration for categories and their associated keywords
    config = {
        "Nature": ["lakeside", "valley", "alp", "sandbar", "cliff", "seashore", "geyser", "volcano", "stone"],
        "Creature": ["gorilla", "gazelle", "bear", "impala", "bison", "orangutan", "baboon", "macaque", "coyote",
                     "boar", "warthog", "dingo", "wolf", "hound", "siamang", "llama", "bighorn", "patas", "wallaby", 
                     "buffalo", "ox", "hartebeest", "ibex", "gibbon"],
        "Vehicle": ["bike", "mobile", "truck", "snowmobile", "jeep", "pickup", "car", "sled", "wagon", "tow", "vehicle",
                    "bicycle", "van"],
        "Tool": ["saw", "hatchet", "shovel", "rifle", "chain", "paddle", "tent", "plow", "uniform", "canoe"]
    }

    # Load data and count entities
    df = pd.read_csv(file_path, sep='\t', usecols=['Detected Objects'])
    entity_counts = df['Detected Objects'].str.split(', ').explode().value_counts()
    filtered_entities = entity_counts[entity_counts > min_count]

    # Categorize each entity
    categorized_data = [
        {
            "name": item,
            "count": count,
            "category": next((cat for cat, keywords in config.items() if any(kw in item for kw in keywords)), "Other")
        }
        for item, count in filtered_entities.items()
    ]

    # Write to JSON file
    with open(output_json_file, 'w') as file:
        json.dump(categorized_data, file, indent=4)

    return categorized_data

# Example usage
file_path = 'Data/reports_v3.tsv'
categorized_entities = process_entities(file_path)
