import pandas as pd

# Load the dataset from a TSV file
bigfoot_df = pd.read_csv('dataset1/reports_task4-c_last.tsv', sep='\t', encoding='utf8')

# Group the data by 'County' and sum up the 'Witness Count' for each county
county_witness_counts = bigfoot_df.groupby('County')['Witness Count'].sum()

# Identify the top 10 counties with the highest witness counts
top10_counties = county_witness_counts.nlargest(10).index

# Mark rows as belonging to a 'BigFoot Hotspot' if their county is in the top 10
bigfoot_df['BigFoot Hotspot'] = bigfoot_df['County'].isin(top10_counties)

# chk
# len(bigfoot_df)
# len(bigfoot_df.loc[bigfoot_df['BigFoot Hotspot']])

# Save the updated DataFrame back to a TSV file
bigfoot_df.to_csv('dataset1/reports_task4-d_last.tsv', sep='\t', index=False)
