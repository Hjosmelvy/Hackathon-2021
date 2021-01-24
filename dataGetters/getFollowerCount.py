#Gets followerCount and twitterAccountId based off of companyTwitterAccounts.csv . Outputs to cvs
# This runs so damn slow, but it works
# ToDo: API request optimization

import requests
import json
import csv
import numpy as np

twitterAccountIds = []
rawTwitterAccountNames = []
twitterAccountNames = []
followerCount = []
foramattedFollowerCount = []
companyNames = []
rawCompanyNames = []

# vvvvvvvvvv ------ Open cvs  file ------- vvvvvvvvvvvvv 
with open('data\companyTwitterAccounts.csv', 'r') as csvfile:
    sample = csvfile.read(64)
    has_header = csv.Sniffer().has_header(sample)
    deduced_dialect = csv.Sniffer().sniff(sample)

with open('data\companyTwitterAccounts.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, deduced_dialect)

    for row in reader:
        if(row[2] != 'Twitter_Account'):
            rawCompanyNames.append(row[1])
            rawTwitterAccountNames.append(row[2])
# ^^^^^^^^^^^^ ------ Open cvs  file ------- ^^^^^^^^^^^ 

twitterAccountsString = ','.join(rawTwitterAccountNames)


index=0
for account in rawTwitterAccountNames:
    if(account == "null"):
        index =index+1
        continue
    else:
         twitterAccountJSON = json.loads(requests.get("https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=" + account).text)
    print(account)
    if(len(twitterAccountJSON) !=0 ):
        twitterAccountIds.append(twitterAccountJSON[0]['id'])
        followerCount.append(twitterAccountJSON[0]['followers_count'])
        foramattedFollowerCount.append(twitterAccountJSON[0]['formatted_followers_count'])
        twitterAccountNames.append(rawTwitterAccountNames[index])
        companyNames.append(rawCompanyNames[index])
    index =index+1
 



    



def outputToCSV():
    rawData =  [twitterAccountIds, twitterAccountNames, companyNames, followerCount, foramattedFollowerCount]
    fields =  ["twitterAccountIds", "twitterAccountNames", "companyNames", "followerCount", "foramattedFollowerCount"]          
    rows = [list(rows) for rows in zip(*rawData)]      # Makes the three lists into one 
    
    filename ="companyTwitterFollowers.csv"
    with open(filename, 'w', newline='') as csvfile:  
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows) 
    
    print("Done!")
outputToCSV()

