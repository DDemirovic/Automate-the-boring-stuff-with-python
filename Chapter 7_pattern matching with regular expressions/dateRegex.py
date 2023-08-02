#! python3

import re

#appends match[number] to an empty list => ignoring all other subgroups which are found with that regex (regular expression)
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

def dateChecker(someDay, someMonth, someYear):
    i = 0
    entriesToDelete = []
    for days in someDay:
        if int(days) < 1 or int(days) > 31:
            entriesToDelete.append(i)
        #print(f"2) vor dem zweiten if. int({days}): {int(days)}")
        else: #int(days) > 0 or int(days) < 32:
            #Day range [1,31]. This checks if the month is a viable month (aka a number in range [1,12], if not => delete)
            if int(someMonth[i]) < 1 or int(someMonth[i]) > 12:
                    entriesToDelete.append(i)
            #edge case day 31 => only a few months have 31 days
            if int(days) == 31:
                #check for months NOT having 31 days, if so => delete
                if int(someMonth[i]) == 2 or int(someMonth[i]) == 4 or int(someMonth[i]) == 6 or int(someMonth[i]) == 9 or int(someMonth[i]) == 11:
                    entriesToDelete.append(i)
            #edge case 29th day in february
            if int(days) == 29:
                #if it's the 29th day in month 2 (aka February) => check if the year is a leap year, if not => delete
                if int(someMonth[i]) == 2:
                    if isLeapYear(int(someYear[i])) == False:
                        entriesToDelete.append(i)
        i += 1
    return entriesToDelete

def deleteEntries(alldates, someDay, someMonth, someYear, entriesList):
    for entry in reversed(entriesList):
        del allDates[entry]
        del someDay[entry]
        del someMonth[entry]
        del someYear[entry]
    return someDay, someMonth, someYear

string = """
i = 0 Dinos Geburtstag ist am 19.04.1993.
i = 1 Noras Geburtstag ist am 27/5/1999. 
i = 2 Emilis Geburtstag ist am 19/2/2004. 
i = 3 Mirzas Geburtstag ist am 4/07/2008.
Falsches Datum 12/2000 welches hoffentlich von der Regex gefiltert wird.
i = 4 Falsches Datum mit falschem Tag -5/11/2000.
i = 5 Falsches Datum mit non-existenten Tag 31/02/2000.
i = 6 Falsches Datum mit keinem Schaltjahr 29/02/2001.
i = 7 Falsches Datum mit 31. Tag im falschen Monat 31/11/1975.
i = 8 Falsches Datum mit falschem Monat 11/13/2000.
i = 9 Falsches Datum mit falschem Monat 12/0/1927.
i = 10 komplett falsches Datum 77/22/3081.
i = 11 negativer Monat 12/-5/2022
"""

#create regex for dates
dateRegex = re.compile(r'''                       #Generally: this pattern should group only the whole date, the day, the month and the year (4 matches in total), indicated by (?:)
                                                  #Match[0] = full date, match[1] = only day, match[2] = only month, match[3] = only year
                       (
                       ((?:-)?(?:\d)?\d)                #Day, singular days accepted, e.g 4 (because 4.7.2000 is a valid date)
                       (?:/|\.)                   #accepted seperators: "/" and "." (19/04/1993 or 19.04.1993)
                       ((?:-)?(?:\d)?\d)                #Month, same as for days 
                       (?:/|\.)                   #same seperators
                       (\d\d\d\d)                 #year (earliest year allowed: 1000)
                       )                
                       ''', re.VERBOSE)

extractedDates = dateRegex.findall(string)
allDates = appendingExtractedDates(extractedDates,0)
allDays = appendingExtractedDates(extractedDates,1)
allMonths = appendingExtractedDates(extractedDates,2)
allYears = appendingExtractedDates(extractedDates,3)
badEntries = dateChecker(allDays, allMonths, allYears)
deleteEntries(allDates, allDays, allMonths, allYears, badEntries)