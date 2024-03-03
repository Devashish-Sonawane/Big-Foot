# Import the pandas library for data manipulation
import pandas as pd

# Load the dataset from a TSV file
bigfoot_df = pd.read_csv('dataset1/reports_task4-b_last.tsv', sep='\t', encoding='utf8')

# Create a new column 'Multiple Witnesses' to indicate whether there were 2 or more witnesses
bigfoot_df['Multiple Witnesses'] = bigfoot_df['Witness Count'] >= 2

# For rows where 'Class' is missing and there are multiple witnesses, set 'Class' to 'Class B'
bigfoot_df.loc[bigfoot_df['Class'].isna() & bigfoot_df['Multiple Witnesses'], 'Class'] = 'Class B'

# Save the updated DataFrame to a TSV file
bigfoot_df.to_csv('dataset1/reports_task4-c_last.tsv', sep='\t', index=False)
