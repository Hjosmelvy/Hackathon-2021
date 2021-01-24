# iterates through a list of top 1000 most searched companies on twitter.
# The website header 'o=#' goes from 0-900 and goes up by 100. 
# This script scapes company name, and twitter handler and outputs to csv
# NOTE: Some handlers and and all follower counts are outdated. So follower counts will be looked up on an api
# To Do: figure a way to get updated twitter accounts

import requests
import csv
from bs4 import BeautifulSoup

companyIDs = []
companyNames = []
companyTwitterAccounts = []

def appendData(): # appends data to the three lists above this comment (companyIDs, companyNames, companyTwitterAccounts)
    for pageNumber in range(0,1000,100):
        URL = 'https://www.theofficialboard.com/twitter/companies?order=&o=' + str(pageNumber)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        soup.prettify()
        rawCompanyRows = soup.find_all('tr',{"class":"twitter-list-row"})

        for rawCompanyRow in rawCompanyRows:
            if(rawCompanyRow.find('span',{"class":"label"}).parent.previous_element.previous_element.previous_element.previous_sibling.text != ''): #when checking for twitter account, check the if the site is able to collect data from the account 
                #^^^^^ this reduces the about of outdated handles that show up in our data to a non-zero number. ^^^ 
                #Finding the element this way is very hacky, but it works
                #In the website, ive noticed that if the table row doesnt have a follower count (its an empty string), it means the twitter account is set to private or deleted
                companyTwitterAccounts.append(rawCompanyRow.find('span',{"class":"label"}).text[8:])
            else:
                companyTwitterAccounts.append("null")

            companyIDs.append(rawCompanyRow.td.text)
            companyNames.append(rawCompanyRow.find('a').text)


def outputToCSV():
    rawData = [companyIDs, companyNames, companyTwitterAccounts]
    fields = ["ID", "Company_Name", "Twitter_Account"]            
    rows = [list(rows) for rows in zip(*rawData)]      # Makes the three lists into one 
    
    filename ="companyTwitterAccounts.csv"
    with open(filename, 'w', newline='') as csvfile:  
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows) 
    
    print("Done!")

appendData()
outputToCSV()



 