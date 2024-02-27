import pandas as pd
import us
from datetime import datetime

tsv = pd.read_table('dataset1/reports_task4-d_last.tsv')
df = pd.DataFrame(tsv)
df['State Short'] = df['State'].apply(lambda x: us.states.lookup(x).abbr if type(x) != float else x)

tsv = pd.read_csv('data/WeatherEvents_Jan2016-Dec2022.csv')
dfWeather = pd.DataFrame(tsv)

newDates = []
for time in dfWeather["StartTime(UTC)"]:
    my_date = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    my_date = my_date.strftime("%Y-%m-%d")
    newDates.append(my_date)

dfWeather = dfWeather.assign(Formated_date=newDates)
dfWeather = dfWeather.groupby(['State', 'County', 'Formated_date'], as_index=False).first()

# dfWeather.to_csv('dataset1/WeatherEvents_aggregated.csv', index=False)
# dfWeather = pd.read_csv('dataset1/WeatherEvents_aggregated.csv', encoding='utf8')

# check
# len(set(df['County']))  # 1023
# len(set(dfWeather['County']))  # 1100
# len(set(df['County']) & set(dfWeather['County']))  # 697
# len(set(df['Nearest Town']) & set(dfWeather['City']))  # 465
# len(set(df['County']) & set(dfWeather['City']))  # 232
# len(set(df['County']) - (set(df['County']) & set(dfWeather['County'])))  # 326
# len((set(df['County']) - (set(df['County']) & set(dfWeather['County']))) & set(dfWeather['City']))  # 38

bigfoot_df = pd.merge(
    df,
    dfWeather,
    left_on=['State Short', 'County', 'Submitted Date Time'], right_on=['State', 'County', 'Formated_date'], how='left')
# left_on=['County', 'Submitted Date Time'], right_on=['County', 'Formated_date'], how='left')

# check
# bigfoot_df['EventId'].notna().sum()  # 152
# bigfoot_df['EventId'].notna().sum()  # 597
# bigfoot_df['Submitted Year'].apply(lambda x: x >= 2016 and x <= 2022).sum()


bigfoot_df.to_csv('dataset1/reports_task4-e_last.tsv', sep="\t", index=False)
