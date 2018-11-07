import csv
from operator import add

with open("AtpMurder-Assault-Harrasment.csv", "r", encoding="latin1") as dataIn:
    dataframe = list(csv.reader(dataIn))

divisionsList = ["Cavan Division", "Monaghan Division", "Donegal Division" , 
            "Sligo Division", "Leitrim Division" , "Louth Division", 
            "Clare Division", "Mayo Division", "Galway Division", 
            "Roscommon Division", "Longford Division", "Cork City Division", 
            "Cork North Division", "Cork West Division", "Kerry Division", 
            "Limerick Division", "Offaly Division", "Laois Division", 
            "Meath Division", "Westmeath Division", "Wicklow Division", 
            "Kildare Division", "Tipperary Division", "Wexford Division", 
            "Carlow Division", "Kilkenny Division", "Waterford Division", 
            "D.M.R South Central Division", "D.M.R North Central Division", 
            "D.M.R Northern Division", "D.M.R Southern Division", 
            "D.M.R Eastern Division", "D.M.R Western Division"]

year = [2003, 2004, 2005, 2006, 2007, 
        2008, 2009, 2010, 2011, 2012, 
        2013, 2014, 2015, 2016, 2017]

#occurances = [[divisionsList, totalCountPerDivision]]

#default values
numberCrimesTotal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
numberCrimes = []

#find rows that are in every division
for row in dataframe:
    for division in divisionsList:
        if division in row[0]:
            numberCrimes.append(row[1:16])

    
#empty list for string to int conv
numberCrimesInt = []

#convert from list of list of strings, to list of list of ints
i=0
for x in numberCrimes:
    while (i<len(numberCrimes)):
        numberCrimesInt.append([int(i) for i in x])
        i += 1
        break

#add all rows together to make one list of ints
i=0
while (i<len(numberCrimesInt)):
    numberCrimesTotal = map(add, numberCrimesTotal, numberCrimesInt[i])
    i += 1

#
print(list(numberCrimesTotal))

'''
print(list(numberCrimesTotal))
print(len(numberCrimes))
print(len(numberCrimesInt))
print(len(list(numberCrimesTotal)))

print(list( map(add, numberCrimesTotal, numberCrimes[0])))
print(count)


i=0
while (i<len(numberCrimes)):
    #print(numberCrimes[i])
    i += 1

i=0
while (i<len(numberCrimesInt)):
    #print(numberCrimesInt[i])
    i += 1
'''
