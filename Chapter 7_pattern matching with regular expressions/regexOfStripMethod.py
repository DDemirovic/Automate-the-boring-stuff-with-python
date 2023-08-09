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
        toStripCharacterStart = "^("
        toStripCharacterEnd = ")+$"
        i = 0
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
        toStripCharacterStart = toStripCharacterStart + ")+"
        toStripCharacterEnd = "(" + toStripCharacterEnd
        print(f"toStripCharacterStart: {toStripCharacterStart}\ntoStripCharacterEnd: {toStripCharacterEnd}")
        return toStripCharacterStart, toStripCharacterEnd
    
    

#stripping off the string
def strippingOffString(string, stripRegexStart, stripRegexEnd):
    startRegex = re.compile(stripRegexStart)
    string = startRegex.sub("", string)
    endRegex = re.compile(stripRegexEnd)
    string = endRegex.sub("", string)
    return string

myString = "    Hier bist mein Text der hoffentlich ausgetauscht wird   "
myStripRegexStart,myStripRegexEnd = strippingRegex()
print(f"myStripRegexStart: {myStripRegexStart}\nmyStripRegexEnd: {myStripRegexEnd}")
myString = strippingOffString(myString, myStripRegexStart, myStripRegexEnd)
print(myString)