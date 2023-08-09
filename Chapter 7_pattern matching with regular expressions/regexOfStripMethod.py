#! python 3

import re

#strip regex
def strippingRegex():
    toStripCharacter = input('Please enter the characters you want deleted: ')
    #if no user input => fill in a space character
    if toStripCharacter == '':
        toStripCharacterStart = "^\s+"
        toStripCharacterEnd = "\s+$"
        return toStripCharacterStart, toStripCharacterEnd
    else:
        #initializing regex start and end
        toStripCharacterStart = "^("            #template: ^(...)
        toStripCharacterEnd = ")+$"             #template: (...)$
        i = 0
        #loop that iterates over every character of that string
        for character in toStripCharacter:
            #regex cannot start with a | => e.g ^(|e|x|a|m|p|l|e), this is an invalid regex
            if 0 == i:
                #adding cases for special characters: whitespace and "." 
                if " " == character:
                    toStripCharacterStart = toStripCharacterStart + "\s"
                    toStripCharacterEnd = "|\s" + toStripCharacterEnd
                elif "." == character:
                    toStripCharacterStart = toStripCharacterStart + "\."
                    toStripCharacterEnd = "|\." + toStripCharacterEnd
                else:
                    toStripCharacterStart = toStripCharacterStart + character
                    toStripCharacterEnd = "|" + character + toStripCharacterEnd
            else:
                #adding cases for special characters: whitespace and "." 
                if " " == character:
                    toStripCharacterStart = toStripCharacterStart + "|\s"
                    toStripCharacterEnd = "|\s" + toStripCharacterEnd
                elif "." == character:
                    toStripCharacterStart = toStripCharacterStart + "|\."
                    toStripCharacterEnd = "|\." + toStripCharacterEnd
                else:
                    toStripCharacterStart = toStripCharacterStart + "|" + character
                    toStripCharacterEnd = "|" + character + toStripCharacterEnd
            i += 1
        #finishing start and end regex
        toStripCharacterStart = toStripCharacterStart + ")+"
        toStripCharacterEnd = "(" + toStripCharacterEnd
        return toStripCharacterStart, toStripCharacterEnd   
        
#stripping off the string
def strippingOffString(string, stripRegexStart, stripRegexEnd):
    startRegex = re.compile(stripRegexStart)
    string = startRegex.sub("", string)
    endRegex = re.compile(stripRegexEnd)
    string = endRegex.sub("", string)
    return string

myString = "    Hier bist mein Text der hoffentlich ausgetauscht wird.   "
myStripRegexStart,myStripRegexEnd = strippingRegex()
myString = strippingOffString(myString, myStripRegexStart, myStripRegexEnd)
print(myString)
