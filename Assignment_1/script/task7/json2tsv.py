import json
import pandas as pd

# Set the directory path where the JSON files are stored
dir_path = 'dataset1/output/'
concatenated_content = ''
# Loop through each JSON file by number and concatenate their content
for i in range(1, 4374):
    file_path = dir_path + 'chunk' + str(i) + '.json'
    with open(file_path, 'r') as f:
        concatenated_content += f.read().strip()

# Load the concatenated JSON content into a Python object
json_data = json.loads(concatenated_content)
# Convert the 'BFRO' part of the JSON data into a pandas DataFrame
df = pd.DataFrame(json_data['BFRO'])
# Rename specific columns to remove trailing spaces for consistency
df.rename(columns={'Nearest Town  ': 'Nearest Town', 'Location Details ': 'Location Details', 'Observed.1  ': 'Observed.1'}, inplace=True)

# Define the desired order of rows in the DataFrame
row_order = [
    'Report Type', 'Id', 'Class', 'Submitted Date', 'Headline', 'Year', 'Season', 'Month', 'State', 'County', 'Location Details',
    'Nearest Town', 'Nearest Road', 'Observed', 'Also Noticed', 'Other Witnesses', 'Other Stories', 'Time And Conditions',
    'Environment', 'Follow-Up', 'Follow-Up Report', 'Date', 'Author', 'Media Source', 'Source Url', 'Media Issue', 'Observed.1',
    'A & G References', 'Submitted Date Time', 'Submitted Year', 'Fixed Year', 'Location', 'State Short', 'Formatted Address',
    'Nearest NP', 'National Park Visitation Count', 'Witness Count', 'Multiple Witnesses', 'BigFoot Hotspot', 'Year-Month',
    'StartTime', 'EventId', 'Severity', 'EndTime', 'TimeZone', 'AirportCode', 'City', 'ZipCode', 'index', 'Type', 'Precipitation(in)',
    'LocationLat', 'LocationLng', 'Gallons of ethanol (absolute alcohol)', 'Population (age 14 and older)',
    'Gallons of ethanol per capita age 14 and older', 'Decile for per capita consumption age 14 and older', 'Population (age 21 and older)',
    'Gallons of ethanol per capita age 21 and older', 'Decile for per capita consumption age 21 and older', 'Gallons of ethanol derived from time-varying ABV',
    'State Resident Population', 'State Population Density', 'Census Rank', 'MAMMAL 1', 'YEAR 1', 'foot size', 'MAMMAL 2', 'YEAR 2',
    'foot size.1', 'MAMMAL 3', 'YEAR 3', 'foot size.2', 'MAMMAL 4', 'YEAR 4', 'foot size.3', 'id', 'jaccard_score'
]

# Reorder the DataFrame according to 'row_order'
df = df[row_order]
# Convert the 'Id' column to integers
df['Id'] = df.apply(lambda r: int(r['Id']), axis=1)

# Load the task5 final dataset
df_task5 = pd.read_csv('dataset1/reports_task5.tsv', sep='\t', encoding='utf8')
# Merge 'df_task5' with selected columns from 'df', removing duplicates based on 'Id' and 'Headline'
# and performing a left join to keep all rows from 'df_task5'
df_task7 = pd.merge(df_task5, df[['Id', 'Headline', 'id', 'jaccard_score']].drop_duplicates(subset=['Id', 'Headline']), on=['Id', 'Headline'], how='left')

# Save the merged DataFrame to a TSV file, without the index
df_task7.to_csv('dataset1/reports_task7.tsv', sep='\t', index=False)
