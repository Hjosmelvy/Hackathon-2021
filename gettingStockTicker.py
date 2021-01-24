#Gets stock ticker based off of company name
#Outputs as csv

import requests
import json
import csv

rawCompanyNames =[]
companyNames =[]
companySymbols = []
companyExchs = []
companyExchsDisplay = []
index =0
with open('data\companyTwitterFollowers.csv', 'r') as csvfile:
    sample = csvfile.read(64)
    has_header = csv.Sniffer().has_header(sample)
    deduced_dialect = csv.Sniffer().sniff(sample)

with open('data\companyTwitterFollowers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, deduced_dialect)

    for row in reader:
        if(row[2] != 'companyNames'):
            rawCompanyNames.append(row[2])

for companyName in rawCompanyNames:

    URL = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query="+ companyName +"&region=1&lang=en"
    response = json.loads(requests.get(URL).text)
    
    if(len(response["ResultSet"]["Result"]) != 0):
        
        companyNames.append(rawCompanyNames[index])
        companySymbols.append(response["ResultSet"]["Result"][0]["symbol"])
        companyExchs.append(response["ResultSet"]["Result"][0]["exch"])
        companyExchsDisplay.append(response["ResultSet"]["Result"][0]["exchDisp"])
        print(rawCompanyNames[index])
    index = index + 1


rawData = [companySymbols, companyNames, companyExchs, companyExchsDisplay] 
rows = [list(rows) for rows in zip(*rawData)]      # Makes the three lists into one 

print(rows)
