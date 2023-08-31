#! python3
   # madlibs.py - program that reads text files and lets the user add their own text anywhere the word "adjective", "noun", "adverb", "verb" appears

import pyinputplus as pyip
import re
import pathlib

#function that extracts content from a file - takes a string that contains the path of that file
def extractingContent(filePath):
   madLibsFile = open(myFilePath)
   madLibsText = madLibsFile.read()  #readlines() returns a list containing each line as an entry - not needed for this task
   madLibsFile.close()
   return madLibsText

#function that creates a regex and searches for that regex - returns an integer of how many matches were found - takes a string (for the regex) as an argument
def regexSearch(regex):
   global fileContent
   searchRegex = re.compile(regex)
   numberOfMatches = searchRegex.findall(fileContent)
   return len(numberOfMatches)

#function that prints the number of matches - takes an int and a string as an argument
def printNumberOfMatches(numberOfMatches, regex):
   if numberOfMatches > 1:
      print(f"{numberOfMatches} {regex.lower()}(s) found")

#function that substitutes text with user input - takes an int (how many iterations we need) and a string (word that needs to be subbed out) as an argument
def regexSub(numberOfMatches, regex):
   global fileContent
   if numberOfMatches >= 1:
      for _ in range(1,numberOfMatches + 1):
         wordsLeft = (numberOfMatches + 1) - _
         userInput = pyip.inputStr(f"{wordsLeft} {regex.lower()}(s) left.\nEnter a {regex.lower()}: ")
         fileContent = re.sub(regex, userInput, fileContent, count = 1) #count = 1 because there's possibly more than one of that regex in the text and we only want to change the first one

#function that writes content in a file
def writingResult():
   global fileContent
   madLibsFinal = open("madLibsFinal.txt", "w") #.txt in cwd (current working directory)
   madLibsFinal.write(fileContent)
   madLibsFinal.close()

myFilePath = pathlib.Path("C:\\Users\\ddemirovic\\Desktop\\Yep\\madLibs.txt") #not really necessary to safe the path in a variable (currently I am not doing anything with that variable)
fileContent = extractingContent(myFilePath)

howManyMatches = regexSearch("NOUN")
printNumberOfMatches(howManyMatches, "NOUN")
regexSub(howManyMatches, "NOUN")

howManyMatches = regexSearch("ADJECTIVE")
printNumberOfMatches(howManyMatches, "ADJECTIVE")
regexSub(howManyMatches, "ADJECTIVE")

howManyMatches = regexSearch("VERB")
printNumberOfMatches(howManyMatches, "VERB")
regexSub(howManyMatches, "VERB")

howManyMatches = regexSearch("ADVERB")
printNumberOfMatches(howManyMatches, "ADVERB")
regexSub(howManyMatches, "ADVERB")

writingResult()