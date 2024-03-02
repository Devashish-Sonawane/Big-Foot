import re
import tika
from tika import parser
import pandas as pd
import numpy as np

def merge_pdf(tsv):

    # Extract the content from the Population pdf dataset with tika
    tika.initVM()
    parsed = parser.from_file('data/population-density-data-table.pdf')
    x = parsed["content"]

    # Remove the unwanted content. Only keep the values from the tables.
    start = [m.start() for m in re.finditer('Alabama', x)]
    end = [m.start() for m in re.finditer('United States', x)]
    data = ""
    for i in range(4):
        data += x[start[i]:end[i]]

    # Clean the data to facilitate the creation of arrays and tables
    data = data.replace("\n\n", " ")
    data = data.replace("\n", " ")
    data = data.replace(",", "")
    data = data.replace("District of ", "")
    data = data.replace("New ", "New_")
    data = data.replace("North ", "North_")
    data = data.replace("South ", "South_")
    data = data.replace("West ", "West_")
    data = data.replace("Rhode ", "Rhode_")
    data = data.split(' ')

    # Create a List of Lists.
    # Each list corresponds to a state and its census data for all decades available
    chunks = [data[x:x+10] for x in range(0, len(data)-1, 10)]
    complete = []
    for i in range(51):
        name = chunks[51+i].pop(0)
        chunks[102+i].pop(0)
        chunks[153+i].pop(0)
        if "_" in name:
            name = name.replace("_", " ")
        fuse = chunks[i]+chunks[51+i]+chunks[102+i]+chunks[153+i]
        decade=0
        for j in range(2021,1904,-1):
            complete.append([name, j]+fuse[1+decade:4+decade])    
            if j in range(1916, 2020, 10):
                decade += 3

                
    #tsv = pd.read_table('dataset1/reports_task5.tsv', encoding='utf8')
    #df = pd.DataFrame(tsv)

    # Create Census panda's DataFrame
    col = ['State', 'Fixed Year', 'State Resident Population', 'State Population Density', 'Census Rank']
    df2 = pd.DataFrame(complete, columns = col) 

    # Merge the Census dataset with the bigfoot dataset (tsv).
    # Merged done by comparing year and state
    bigfoot_df = pd.merge(
        tsv,
        df2[['State', 'Fixed Year', 'State Resident Population', 'State Population Density', 'Census Rank']],
        left_on=['State', 'Fixed Year'], right_on=['State', 'Fixed Year'], how='left')

    # Return Merged dataset
    return bigfoot_df
#bigfoot_df.to_csv('dataset1/reports_task5.tsv', sep="\t", index=False) 

