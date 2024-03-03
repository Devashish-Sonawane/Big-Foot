# Import necessary libraries
import numpy as np
import pandas as pd
import us
from datetime import datetime

# Load the Bigfoot sighting reports dataset from a TSV file into a pandas DataFrame
tsv = pd.read_table('dataset1/reports_task4-d_last.tsv')
df = pd.DataFrame(tsv)

# Convert full state names in the 'State' column to their corresponding abbreviations using the 'us' library
df['State Short'] = df['State'].apply(lambda x: us.states.lookup(x).abbr if type(x) != float else x)

# Create a mapping of month names to their numerical values
month_map = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

# Convert 'Year' and 'Month' columns to a 'Year-Month' datetime format
df['Year-Month'] = df.apply(
    lambda row: datetime(row['Fixed Year'], month_map[row['Month']], 1).strftime('%Y-%m') if type(row['Fixed Year']) == int and type(row['Month']) == str else np.nan, axis=1)

# Load weather events data from a CSV file into a pandas DataFrame
tsv = pd.read_csv('data/WeatherEvents_Jan2016-Dec2022.csv')
dfWeather = pd.DataFrame(tsv)

# Convert 'StartTime(UTC)' and 'EndTime(UTC)' columns to 'Year-Month' format
newDates = []
newDates2 = []
for (time, time2) in zip(dfWeather["StartTime(UTC)"], dfWeather["EndTime(UTC)"]):
    my_date = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    my_date2 = datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    my_date = my_date.strftime("%Y-%m")
    my_date2 = my_date2.strftime("%Y-%m")
    newDates.append(my_date)
    newDates2.append(my_date2)

# Rename columns and assign the new date formats
dfWeather = dfWeather.rename(columns={"StartTime(UTC)": "StartTime", "EndTime(UTC)": "EndTime"})
dfWeather = dfWeather.assign(StartTime=newDates)
dfWeather = dfWeather.assign(EndTime=newDates2)

# Sort the weather data by 'State', 'County', and 'StartTime'
dfWeather = dfWeather.sort_values(['State', 'County', 'StartTime'])

# Calculate the most frequent 'Severity' for each 'State', 'County', and 'StartTime' combination
pre = ''
severity = ['Light', 'Severe', 'Moderate', 'Heavy', 'UNK', 'Other']
sevL = []
remain = False
count = [0, 0, 0, 0, 0, 0]
for sta, cou, date, s in zip(dfWeather['State'], dfWeather['County'], dfWeather['StartTime'], dfWeather["Severity"]):
    if pre == (sta, cou, date):
        # Increment count based on severity
        if s == 'Light':
            count[0] += 1
        if s == 'Severe':
            count[1] += 1
        if s == 'Moderate':
            count[2] += 1
        if s == 'Heavy':
            count[3] += 1
        if s == 'UNK':
            count[4] += 1
        if s == 'Other':
            count[5] += 1
        remain = True
    else:
        # Append the most frequent severity and reset count
        pre = (sta, cou, date)
        sevL.append(severity[pd.Series(count).idxmax()])
        count = [0, 0, 0, 0, 0, 0]
        remain = False
# Handle the last entry
if remain:
    sevL.append(severity[pd.Series(count).idxmax()])
sevL.pop(0)  # Remove the first placeholder entry

# Assign the most frequent severity to each entry in the DataFrame
index = -1
pre = ''
sevMax = []
for sta, cou, date in zip(dfWeather['State'], dfWeather['County'], dfWeather['StartTime']):
    if pre != (sta, cou, date):
        index += 1
        pre = (sta, cou, date)
    sevMax.append(sevL[index])
dfWeather = dfWeather.assign(Severity=sevMax)
dfWeather = dfWeather.rename(columns={"Severity": "Severity Max"})

# dfWeather.to_csv('dataset1/WeatherEvents_aggregated.csv', index=False)
# dfWeather = pd.read_csv('dataset1/WeatherEvents_aggregated.csv', encoding='utf8')

# Aggregate weather data by 'State', 'County', and 'StartTime', calculating averages for numeric columns
type_count_df = dfWeather.groupby(['State', 'County', 'StartTime'])['Type'].value_counts().rename('Type Count').reset_index()
type_count_df = type_count_df.sort_values('Type Count', ascending=False).groupby(['State', 'County', 'StartTime']).head(1).reset_index().drop('Type Count', axis=1)
avg_df = dfWeather.groupby(['State', 'County', 'StartTime'])['Precipitation(in)', 'LocationLat', 'LocationLng'].mean().reset_index()

# check
# len(set(df['County']))  # 1023
# len(set(dfWeather['County']))  # 1100
# len(set(df['County']) & set(dfWeather['County']))  # 697
# len(set(df['Nearest Town']) & set(dfWeather['City']))  # 465
# len(set(df['County']) & set(dfWeather['City']))  # 232
# len(set(df['County']) - (set(df['County']) & set(dfWeather['County'])))  # 326
# len((set(df['County']) - (set(df['County']) & set(dfWeather['County']))) & set(dfWeather['City']))  # 38

# Keep only the first occurrence of each 'State', 'County', 'StartTime' combination and drop unused columns
dfWeather = dfWeather.groupby(['State', 'County', 'StartTime'], as_index=False).first()  # Keep this at the end
dfWeather = dfWeather.drop(['Type', 'Precipitation(in)', 'LocationLat', 'LocationLng'], axis=1)

# Merge the weather data with the Bigfoot sighting reports based on state, county, and date
len(dfWeather)  # 126018
dfWeather = pd.merge(dfWeather, type_count_df, on=['State', 'County', 'StartTime'])
dfWeather = pd.merge(dfWeather, avg_df, on=['State', 'County', 'StartTime'])
len(dfWeather)  # 126018
dfWeather = dfWeather.rename(columns={'Year': 'Weather Year', 'State': 'State Short'})
bigfoot_df = pd.merge(
    df,
    dfWeather,
    left_on=['State Short', 'County', 'Year-Month'], right_on=['State Short', 'County', 'StartTime'], how='left')
# left_on=['County', 'Submitted Date Time'], right_on=['County', 'Formated_date'], how='left')

# check
# bigfoot_df['EventId'].notna().sum()  # 152
# bigfoot_df['EventId'].notna().sum()  # 597
# bigfoot_df['Submitted Year'].apply(lambda x: x >= 2016 and x <= 2022).sum()

# Save the merged dataset to a TSV file
bigfoot_df.to_csv('dataset1/reports_task4-e_last.tsv', sep="\t", index=False)
