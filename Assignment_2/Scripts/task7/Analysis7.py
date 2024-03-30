import math
import pandas as pd

# Load TSV
tsv = pd.read_table('Dataset1/reports_v2_task7.tsv')
df = pd.DataFrame(tsv)

# Variables definitions
df2 = df
dic ={}
lis = [0,0,0]
lis2 = [0,0,0]
dif=[]
fd = []

# Iterate rows
i=0
for row in df['Geographic Locations']:
    
    dists = [] 
    
    # Check NaN locations
    ll = False
    if not isinstance(df['Location'][i], float):
        ll = tuple(map(float, df['Location'][i].replace("(","").replace(")","").split(', ')))
    
    # Check Class
    s = str(df['Class'][i])
    if "Class A" in s:
        lis2[0] = lis2[0] +1
    elif "Class B" in s:
        lis2[1] = lis2[1] +1
    elif "Class C" in s:
        lis2[2] = lis2[2] +1

    val = eval(row).values()
    for x in val:
        for y,z in x.items():
            # Count Geoparser Locations num and locations/class
            if y=='Name':
                if z in dic.keys():
                    dic[z]=dic[z]+1
                else:
                    dic[z]=1
        
                if "Class A" in s:
                    lis[0] = lis[0] +1
                elif "Class B" in s:
                    lis[1] = lis[1] +1
                elif "Class C" in s:
                    lis[2] = lis[2] +1      
            
            # Load Geoparser Lat/Lon
            if ll:
                if y== 'Latitude':
                    aux= float(z)
                elif y== 'Longitude':
                    aux2= float(z)
               
        # Euclidean distance
        if ll:
            f1 = [ll[0], ll[1]]
            f2 = [aux, aux2]
            dists.append(math.dist(f1, f2))
    
    # Min euclidean in the row       
    if dists:
        fd.append(min(dists))        
    i=i+1
    
print("Avg euclidean distance min(Loaction sighting/Location parser):")
print(sum(fd)/len(fd))


print("\nAvg locations per class (A,B,C):")
print(lis[0]/lis2[0],lis[1]/lis2[1], lis[2]/lis2[2])

print("\nLocations ordered by number of apperances:")
print(sorted(dic.items(), key=lambda x:x[1], reverse=True))