try:
    import pandas as pd
    import json
    import re
    import logging
except ImportError as e:
    print(f"Error importing required libraries: {e}")
    exit(1)
logging.basicConfig(level=logging.INFO)

def create_json(input_filename, output_filename):
    try:
        df = pd.read_csv(input_filename, sep='\t') # Making dataframe of input file
        logging.info("Successfully, Converted the input file to a dataframe.")
        values_set = set(df['State'].unique()) | set(df['Season'].unique()) | set(df['County'].unique()) # Making sets of column values
        values_set = {value for value in values_set if re.match('^[a-zA-Z]+$', str(value))}
        values_set = {value for value in values_set if value is not None and value != ""}
        logging.info(" I am going to start counting number of sightings in each county.")

        # Calculating the score for each county (No. sightings in each county)
        county_scores = {}
        for value in values_set:
            score = df[df['County'] == value].shape[0]
            county_scores[value] = score
        logging.info("I have finished calculating score. Now I will create the JSON format.\nThis can take a while (5-10 mins).")

        # Constructing JSON format required for the Visualization
        data = {
            "name": "Seasons",
            "children": []
        }
        for season in set(df['Season']):
            season_data = {
                "name": season,
                "children": []
            }
            for state in set(df['State']):
                state_data = {
                    "name": state,
                    "children": []
                }
                counties_added = False
                for county in set(df['County']):
                    if county_scores.get(county, 0) > 0 and df[(df['Season'] == season) & (df['State'] == state) & (df['County'] == county)].shape[0] > 0:
                        if not pd.isnull(county):  # Check if county is not NaN
                            county_data = {
                                "name": county,
                                "value": county_scores.get(county, 0)
                            }
                            state_data["children"].append(county_data)
                            counties_added = True
                if counties_added:
                    season_data["children"].append(state_data)
            if season_data["children"]:  # Check if any states were added to the season
                data["children"].append(season_data)

        logging.info("I will now convert the data to json")
        # Write the JSON data to output file
        with open(output_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Hey, your output file: ({output_filename}) has been generated.")

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        print(f"An error occurred: {str(e)}")

input = r"..\Data\reports_v3.tsv"
output = r"visualization_4.json"
create_json(input, output)