#! python 3
#! regexSearch.py - a program that scans .txt files in a specified folder for a user-supplied regex

import re
import pathlib
import pyinputplus as pyip

#function that extracts content from .txt files: exctracts A) name of txt file(s) and B) the corresponding text (in a dict) - takes a path as an argument (a real path, not only a string of that path), returns a dict
def exctractContentOfFile(aPath):
    extractedContentDict = {}   #dictionary that gets filled with name and content
    #loop that iterates over .txt files
    for textFile in aPath.glob('*.txt'):
        stringOfTextFilePath = ('\\'.join([str(aPath), str(textFile.name)]))    #saving whole path of each text file, just to make sure there's no confusion which text file needs to be read
        pathOfFile = pathlib.Path(stringOfTextFilePath)                         #saving it as a path variable
        contentOfFile = pathOfFile.read_text()                                  #reading content of .txt file
        extractedContentDict.update({str(textFile.name) : contentOfFile})       #saving key = name.txt and value = content of txt file in a dictionary
    return extractedContentDict

#function that is scanning the content - takes a dictionary (contentDictionary), a string (regex) and two bools (occurence, ignoreCase) as an argument, returns a list with files that meets the given conditions
#occurence means: do we accept a regex return for e.g 'a' in 'automation'? If yes, occurence = True, otherwise occurence = False
def searchingContent(contentDictionary, regex, occurence, ignoreCase):
    #compiles the regex in such a way, that it ignores lower/upper case and accepts occurences, e.g: 'a' in 'automation'
    if occurence and ignoreCase:
        searchRegex = re.compile(regex, re.IGNORECASE)
    elif occurence:
        searchRegex = re.compile(regex)
    elif ignoreCase:
        regex = r" " + regex + r" "     #putting whitespace "around" the word, ensuring we do not find results for 'a' in e.g = 'automation' 
        searchRegex = re.compile(regex, re.IGNORECASE)
    else:
        regex = r" " + regex + r" "     #putting whitespace "around" the word, ensuring we do not find results for 'a' in e.g = 'automation' 
        searchRegex = re.compile(regex)
    filesWithRegex = []
    for key in contentDictionary:
        if re.search(searchRegex, contentDictionary[key]) != None:
            filesWithRegex.append(key)
    return filesWithRegex

#function that takes user input - returns the word we are looking for
def userInput():
    userInputStr = pyip.inputStr("What word do you want to search for? ")
    userInputOccurence = pyip.inputBool("Do you want to search for your word as a whole (enter: False/false/F/f) or are you looking for occurences (enter True/true/T/t) e.g 'a' in 'automation'? ")
    userInputIgnoreCase = pyip.inputBool("Do you care about case sensitivity? If yes enter: True/true/T/t, if no enter: False/false/F/f. ")
    return userInputStr, userInputOccurence, userInputIgnoreCase

#function that prints a list
def printingResults(resultList):
    if len(resultList) >= 1:
        print("Found your word in the following files:")
        for file in resultList:
            print(file)
    else:
        print("Your word hasn't been found in any file.")

#hardcoded path of the files which we wanna scan - obviously change the path if you want to scan other .txt files
myPath = pathlib.Path("G:\\Automate the boring stuff with Python\\Chapter 9 reading and writing files\\bunchOfTextFiles")

myDict = exctractContentOfFile(myPath)
myRegex,myOccurence, myIgnoreCase = userInput()
myList = searchingContent(myDict, myRegex, myOccurence, myIgnoreCase)
printingResults(myList)