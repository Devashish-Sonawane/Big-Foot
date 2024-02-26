import pandas as pd
from datetime import datetime


tsv = pd.read_table('dataset1/reports_task4-d.tsv')
df = pd.DataFrame(tsv)

tsv = pd.read_csv('data/WeatherEvents_Jan2016-Dec2022.csv')
dfWeather = pd.DataFrame(tsv)

newDates = []
for time in dfWeather["StartTime(UTC)"]:
    my_date = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    my_date = my_date.strftime("%Y-%m-%d")
    newDates.append(my_date)

dfWeather = dfWeather.assign(Formated_date=newDates)
dfWeather = dfWeather.groupby(['State', 'County', 'Formated_date'], as_index=False).first()
bigfoot_df = pd.merge(
    df,
    dfWeather,
    left_on=['State Short', 'County', 'Submitted Date Time'], right_on=['State', 'County', 'Formated_date'], how='left')

bigfoot_df.to_csv('dataset1/reports_task4-e_last.tsv', sep="\t", index=False) 
    