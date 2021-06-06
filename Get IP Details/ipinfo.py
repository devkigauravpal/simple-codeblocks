#Author: @devkigauravapal
#Context: Supply list of IPs and a CSV with details will be generated.
#Input CSV will have "IP Address" column header and then list of IP address
import json, urllib.request, csv
import pandas as pd
df = pd.read_csv('IPaddress.csv') #Read IP address into DF
df1=pd.DataFrame()
for index, row in df.iterrows(): # Iterate through IPs
    if row['IP Address'] != '':
        url = 'https://ipinfo.io/' + row['IP Address'] + '/json' #Generating URL for information
    with urllib.request.urlopen(url) as url: #Reading URL data
        s = url.read()
        resp=json.loads(s.decode())
        tempdf=pd.io.json.json_normalize(resp) #Normalize Json
        df1=df1.append(tempdf, ignore_index = True) #Storing in memory temporarily in DF   
df1.to_csv (r'IPaddress_Details.csv',index = None, header=True) #DF to CSV output
