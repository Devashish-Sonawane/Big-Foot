import pandas as pd
import pyperclip
import json
from dateutil.parser import parser
from datetime import datetime as dt
from statistics import mean
import googlemaps
import numpy as np
from urllib.parse import quote
from scipy.spatial import cKDTree

bigfoot_df = pd.read_csv('dataset1/reports.tsv', sep='\t', encoding='utf8')

# ===============================
# section 1: clean year column
# ===============================
# check type of year
year_int = list()
year_str = list()
year_nan = list()
for y in bigfoot_df['Year']:
    try:
        int(y)
    except:
        if type(y) == str:
            year_str.append(y)
        else:
            year_nan.append(y)
    else:
        year_int.append(int(y))
len(year_str)  # 368
len(year_int)  # 4,647
len(year_nan)  # 452

# outlier check
print(sorted(year_int)[:10])  # 5, 7, 7, 8, 76=1976?
print(sorted(year_int)[-10:])  # 20010

# output irregulara string year
print(set(year_str))
pyperclip.copy('\n'.join(set(year_str)))

# generate corresponding year range with chatgpt
with open('script/task4/irregular_year.json') as j:
    ir_year_j = json.load(j)

# Extract year from SUBMITTED DATE for completion
new_columns = {}
new_columns['Submitted Date Time'] = list(map(parser().parse, bigfoot_df['Submitted Date']))
new_columns['Submitted Year'] = list(map(lambda x: x.year, new_columns['Submitted Date Time']))
bigfoot_df = pd.concat([bigfoot_df, pd.DataFrame(new_columns)], axis=1)

# clean year column
fixed_year = list()
for index, row in bigfoot_df[['Year', 'Submitted Year']].iterrows():
    ry = row['Year']
    rsy = row['Submitted Year']
    try:
        int(ry)
    except:
        if type(ry) == str:
            y_range = list(filter(lambda x: x <= rsy, ir_year_j[ry]))
            fixed_year.append(int(mean(y_range)) if y_range else rsy)
        else:  # nan
            fixed_year.append(rsy)
    else:
        fixed_year.append(int(ry) if 1000 <= int(ry) <= 2024 else rsy)
bigfoot_df['Fixed Year'] = fixed_year

# ===============================
# section 2: clean location data
# ===============================
# check
bigfoot_df['State'].isnull().sum()  # 451
bigfoot_df['County'].isnull().sum()  # 451
bigfoot_df['Nearest Road'].isnull().sum()  # 1153
bigfoot_df['Nearest Town'].isnull().sum()  # 773
bigfoot_df['Location Details'].isnull().sum()  # 1212

bigfoot_df['County'][bigfoot_df['State'].isnull()].isnull().sum()  # 451
bigfoot_df['Nearest Road'][bigfoot_df['State'].isnull()].isnull().sum()  # 451
bigfoot_df['Nearest Town'][bigfoot_df['State'].isnull()].isnull().sum()  # 451
bigfoot_df['Location Details'][bigfoot_df['State'].isnull()].isnull().sum()  # 451
# => if county == nan, all other attributes are also nan

# check state name
pyperclip.copy('\n'.join(set(bigfoot_df['State']) - {np.nan}))

gmaps = googlemaps.Client(key='AIzaSyDTplXNvMbpSBI05P2nDCef2B-5J0m6Jk8')


def clean_str(x):
    if type(x) == str:
        return x.replace('\x92', '').replace('\x93', '').replace('\x94', '').replace('\x97', '').replace('\xa0', ' ')
    return x


new_cols = {'Location': list(), 'State Short': list(), 'Formatted Address': list()}
for index, row in bigfoot_df[['State', 'County', 'Nearest Road', 'Nearest Town', 'Location Details']].iterrows():
    print(index)
    if type(row['State']) == float:
        for key in new_cols:
            new_cols[key].append(None)
        continue
    row = row.apply(clean_str)
    params = {'country': 'US', 'administrative_area': row['State'], 'locality': row['County'], 'route': row['Nearest Road']}
    params = {k: v for k, v in params.items() if type(v) != float}
    queries = [row['Nearest Town'], row['Location Details'], '']
    for q in queries:
        if type(q) == float:
            continue
        res = gmaps.geocode(q, components=params)
        filtered_res = [
            item for item in res
            if any(
                component['long_name'] == row['State'] and 'administrative_area_level_1' in component['types']
                for component in item['address_components']
            )
        ]
        if len(filtered_res) != 0:
            break
    if len(filtered_res) == 0:
        for key in new_cols:
            new_cols[key].append(None)
        continue
    new_cols['Location'].append((filtered_res[0]['geometry']['location']['lat'], filtered_res[0]['geometry']['location']['lng']))
    new_cols['State Short'].append(next(
        (component['short_name'] for component in filtered_res[0]['address_components']
         if 'administrative_area_level_1' in component['types'])
        , None))
    new_cols['Formatted Address'].append(filtered_res[0]['formatted_address'])
bigfoot_df = pd.concat([bigfoot_df, pd.DataFrame(new_cols)], axis=1)
bigfoot_df.to_csv('dataset1/reports_task4-a_1.tsv', sep='\t', index=False)
# bigfoot_df = pd.read_csv('dataset1/reports_task4-a_1.tsv', sep='\t', encoding='utf8')
# bigfoot_df['Location'] = bigfoot_df['Location'].str.strip('()').apply(lambda x: tuple(float(e) for e in x.split(', ')) if type(x) == str else x)

# ===================================
# section 3: load national park data
# ===================================
national_park_df = pd.read_excel('data/Query Builder for Public Use Statistics (1979 - Last Calendar Year).xlsx', header=2)
national_park_unique_df = national_park_df.drop_duplicates(subset=['Park']).copy().reset_index(drop=True)

new_cols_NP = {'Location NP': list(), 'Formatted Address NP': list()}
for index, row in national_park_unique_df[['Park', 'State']].iterrows():
    print(index)
    params = {'country': 'US'}
    q = row['Park'].replace('NP', 'National Park')
    res = gmaps.geocode(q, components=params)
    new_cols_NP['Location NP'].append((res[0]['geometry']['location']['lat'], res[0]['geometry']['location']['lng']))
    new_cols_NP['Formatted Address NP'].append(res[0]['formatted_address'])
national_park_unique_df = pd.concat([national_park_unique_df, pd.DataFrame(new_cols_NP)], axis=1)
national_park_unique_df.to_csv('dataset1/national_park_task4.csv', index=False)
# national_park_unique_df = pd.read_csv('dataset1/national_park_task4.csv', encoding='utf8')
# national_park_unique_df['Location NP'] = national_park_unique_df['Location NP'].str.strip('()').apply(lambda x: tuple(float(e) for e in x.split(', ')) if type(x) == str else x)

tree = cKDTree(np.array(national_park_unique_df['Location NP'].values.tolist()))
bigfoot_clean_df = bigfoot_df[['Location']].dropna(subset=['Location']).copy()
distances, indices = tree.query(np.array(bigfoot_clean_df['Location'].values.tolist()), k=1)
bigfoot_clean_df['Nearest NP'] = national_park_unique_df.iloc[indices]['Park'].values
bigfoot_df = bigfoot_df.join(bigfoot_clean_df['Nearest NP'], how='left')

national_park_df = national_park_df.rename(columns={'Year': 'Fixed Year'})
bigfoot_df = pd.merge(
    bigfoot_df,
    national_park_df[['Park', 'Fixed Year', 'Recreation Visits']],
    left_on=['Fixed Year', 'Nearest NP'], right_on=['Fixed Year', 'Park'], how='left')
bigfoot_df.drop(columns=['Park'], inplace=True)
bigfoot_df.rename(columns={'Recreation Visits': 'National Park Visitation Count'}, inplace=True)
bigfoot_df.to_csv('dataset1/reports_task4-a_last.tsv', sep='\t', index=False)
