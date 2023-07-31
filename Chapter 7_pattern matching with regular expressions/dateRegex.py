#! python3

import re

#appends match[0] to an empty list => ignoring all subgroups which are found with that regex (regular expression)
def appendingExtractedDates(someString, number):
    allDates = []
    for dates in someString:
        allDates.append(dates[number])
    return allDates

#function that checks if a given year is a leap year or not
def isLeapYear(someYear):
    if someYear % 400 == 0 or someYear % 4 == 0 and someYear % 100 != 0:
        leapYear = True
    else:
        leapYear = False
    return leapYear

string = "Dinos Geburtstag ist am 19.04.1993. Noras Geburtstag ist am 27/5/1999. Emilis Geburtstag ist am 19/2/2004. Mirzas Geburtstag ist am 4/07/2008.Fiktives falsches Datum 12/2000"
#create regex for dates
dateRegex = re.compile(r'''                       #Generally: this pattern should group only the whole date, the day, the month and the year (4 matches in total), indicated by (?:)
                                                  #Match[0] = full date, match[1] = only day, match[2] = only month, match[3] = only year
                       (((?:\d)?\d)               #Day, singular days accepted, e.g 4 (because 4.7.2000 is a valid date)
                       (?:/|\.)                   #accepted seperators: / and . (19/04/1993 or 19.04.1993)
                       ((?:\d)?\d)                #Month, same as for days 
                       (?:/|\.)                   #same seperators
                       (\d\d\d\d))                #year (earliest year allowed: 1000)
                       ''', re.VERBOSE)
extractedDates = dateRegex.findall(string)
allDates = appendingExtractedDates(extractedDates,0)
allDays = appendingExtractedDates(extractedDates,1)
allMonths = appendingExtractedDates(extractedDates,2)
allYears = appendingExtractedDates(extractedDates,3)
print(allDates)
print(allDays)
print(allMonths)
print(allYears)
