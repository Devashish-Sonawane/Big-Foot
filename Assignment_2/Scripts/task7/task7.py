# encoding: utf-8

import tika.tika
from tika import parser
import pandas as pd
import re
import os

# We extract the task 6 updated dataset
tsv = pd.read_table('Dataset1/reports_v2_task6.tsv')
df = pd.DataFrame(tsv)

# We create a temporary column that combines evry desired string column into a unique sting
obus = ['Headline', 'Location Details', 'State', 'County', 'Nearest Town', 'Nearest Road', 'Observed', 'Other Stories', 
'Environment', 'Follow-Up Report', 'Media Source','Source Url', 'Media Issue', 'Observed.1', 'A & G References', 
'Formatted Address', 'Nearest NP', 'City', 'Image Text', 'Image Caption']
df['text'] = ''
for t in obus:
    df['text'] = df['text'] + '\n'+ df[t].astype(str)
df['Geographic Locations'] = pd.Series(dtype='object')

tika.tika.TikaServerClasspath = 'ner-model:geotopic-mime:tika-server-standard-2.9.1.jar:tika-parser-nlp-package-2.9.1.jar'

# Send a requests to tika for the text created and add response (NAME, LAT, LON) to pandas as a dictionary of dictionaries(Locations)

for i in range(len(df.index)):
    ex = str(df.at[i, 'text'])
    f = open("ex.geot", "w")
    f.write(ex)
    f.close()
    dic = dict()
    try:
        parsed = parser.from_file('ex.geot',requestOptions={'timeout': 300})
        vals = parsed["metadata"]
        for n in vals.keys():
            if 'Geographic' in n:
                if not('Location' in dic.keys()):
                    dic['Location'] = {}
                if 'NAME' in n:
                    dic['Location']["Name"] = vals[n].replace("'","`")
                elif 'LONGITUDE' in n:
                    dic['Location']["Longitude"] = vals[n]
                else:
                    dic['Location']["Latitude"] = vals[n]          
            elif 'Optional' in n:
                aux = 'Optional' + re.sub("[^0-9]", "", n)
                aux = str(aux)
                if not(aux in dic.keys()):
                    dic[aux] = {}
                if 'NAME' in n:
                    dic[aux]["Name"] = vals[n].replace("'","`")
                elif 'LONGITUDE' in n:
                    dic[aux]["Longitude"] = vals[n]
                else:
                    dic[aux]["Latitude"] = vals[n]
        # Follow track of tika requests
        if i % 100 == 0:
            print(i)
    except Exception as e:
        print(e)
    df.at[i, "Geographic Locations"] = dic
os.remove("ex.geot")

# Drop temporal text column and create new tsv 
df.drop(columns=['text'], inplace=True)
df.to_csv('Dataset1/reports_v2_task7.tsv', sep="\t", index=False, encoding='utf-8')         



# Terminals used:

#lucene-geo-gazetteer -server
#java -classpath ner-model:tika-server-standard-2.9.1.jar:tika-parser-nlp-package-2.9.1.jar org.apache.tika.server.core.TikaServerCli
#python2 test.py
