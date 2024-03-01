#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Read BFRO and STATEMAMMAL TSV files
bfro_df = pd.read_csv("/Users/willy/Desktop/Academic/usc/2024 Spring/DSCI550/merged_reports_task5-1.tsv", sep="\t")
statemammal_df = pd.read_csv("/Users/willy/Desktop/Academic/usc/2024 Spring/DSCI550/Task5_image_dataset.tsv", sep="\t")

# Merge BFRO and STATEMAMMAL data on 'State' column
merged_df = pd.merge(bfro_df, statemammal_df, on='State', how='left')

# Select and reorder columns in the desired output format
output_columns = ['State', 'STATE MAMMAL 1', 'YEAR 1', 'SIZE 1', 'STATE MAMMAL 2', 'YEAR 2', 'SIZE 2', 'STATE MAMMAL 3', 'YEAR 3', 'SIZE 3', 'STATE MAMMAL 4', 'YEAR 4', 'SIZE 4']
final_df = merged_df[output_columns]

# Write the final dataframe to a new TSV file
final_df.to_csv("/Users/willy/Desktop/Academic/usc/2024 Spring/DSCI550/output_BFRO.tsv", sep="\t", index=False)

print("Output written to output_BFRO.tsv")


# In[ ]:




