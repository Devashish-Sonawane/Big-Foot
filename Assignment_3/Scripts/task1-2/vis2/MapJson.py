import pandas as pd
import addfips

tsv = pd.read_table('Data/reports_v3.tsv')
df = pd.DataFrame(tsv)


# Dataframe for FIPS (gets all unique combinations, handles Springfield MA, Springfield IL etc.) 
fips = pd.DataFrame(df.groupby(['State', 'County']).size().reset_index().iloc[:,[0,1]])

# Add FIPS code to fips df
af = addfips.AddFIPS()
for index, row in fips.iterrows():
    fips.at[index,'FIPS']=af.get_county_fips(fips.at[index,'County'],fips.at[index,'State'])
    fips.at[index,'FIPSState']=af.get_state_fips(fips.at[index,'State'])

# Add FIPS to data
data = fips.merge(df, how='inner', on=['County', 'State'])

dfj = data[["FIPS","FIPSState"]]
dfjj = dfj.groupby(['FIPS','FIPSState']).size().to_frame(name = 'count').reset_index()
dfjj["count"]=dfjj["count"].astype(str)

lists = dfjj.values.tolist()
listb =[["county", "state", "count"]]
for row in lists:
    listb.append(row)

listc = str(listb)
listc = listc.replace('\'','\"')
listc

with open("sightsCounts.json", "w") as outfile:
    outfile.write(listc)
