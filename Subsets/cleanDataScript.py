#!/usr/bin/python
### Author: Daniel Maguire, 9-11-18
import csv
from operator import add
from numpy import sum

### TURN GARDA STATIONS INTO COUNTIES AND SUM THE RESPECTIVE ROWS TOGETHER
###
### This script will a CSV file, look for irish county in the first column
### (garda stations) overwrite the value with just the county name. 
### Then assuming all other columns are ints, it will sum them all rows 
### with the same county name together.
###
### To use this script, please change the names of the CSV file you wish to
### input and the name of the CSV file you wish to output (lines 12 & 43)

with open("Division - Weapons and Explosives Offences.csv", "r", encoding="latin1") as dataIn:
    dataframe = list(csv.reader(dataIn))

#garda divisions and counties
divisionsList = ["Cavan", "Monaghan", "Donegal" , 
            "Sligo", "Leitrim" , "Louth", 
            "Clare", "Mayo", "Galway", 
            "Roscommon", "Longford", "Cork", "Kerry", 
            "Limerick", "Offaly", "Laois", 
            "Meath", "Westmeath", "Wicklow", 
            "Kildare", "Tipperary", "Wexford", 
            "Carlow", "Kilkenny", "Waterford", 
            "D.M.R South Central Division", "D.M.R North Central Division", 
            "D.M.R Northern Division", "D.M.R Southern Division", 
            "D.M.R Eastern Division", "D.M.R Western Division", "Dublin"]

#convert garda stations into their respective county
#turn everything besides county, into an int as it should be
for row in dataframe:                         
    for division in divisionsList:                  
        if division in row[0]:                      
            row[0] = division
        if "D.M.R" in row[0]:
            row[0] = "Dublin" 
    row[1:] = list(map(int, row[1:]))

#alphabetically sort our dataset after division to county conversion
dataframe.sort()

#default list
totalCountyCrimes = []

#write to our new csv file
with open("County - Weapons and Explosives Offences.csv", 'w', newline='') as cleanedFile:
    wr = csv.writer(cleanedFile, quoting=csv.QUOTE_NONE)
    #counties = 1
    for row in dataframe:
        if not totalCountyCrimes:
            totalCountyCrimes = row
        elif (row[0] == totalCountyCrimes[0]):
            totalCountyCrimes[1:] = sum([totalCountyCrimes[1:],row[1:]], axis=0)
            print(totalCountyCrimes)
        else:
            wr.writerow(totalCountyCrimes)
            totalCountyCrimes = row
            #counties += 1
    wr.writerow(totalCountyCrimes)      #catch the last row after the for loop completes

# to ensure you got all 26 counties, uncomment variable 'counties' above
# print(counties)