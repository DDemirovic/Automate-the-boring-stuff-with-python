#! python 3
#! regexSearch.py - a program that scans .txt files in a specified folder for a user-supplied regex

import re
import pathlib
import os

#hardcoded path of the files which we wanna scan - obviously change the path if you want to scan other .txt files
myPath = pathlib.Path("G:\\Automate the boring stuff with Python\\Chapter 9_reading and writing files\\bunchOfTextFiles")

#loop that iterates over every fileName in the specified path
for fileName in os.listdir(myPath):
    print(fileName)

print(list(myPath.glob('*.txt')))

#das unten stehende benötige ich um .txt files zu filtern
#   dann mit myPath.name nur den Namen der .txt zu kriegen
#       dann diese einzeln öffnen
#           dann diese mit der regex search durchforsten

# >>> p = Path('C:/Users/Al/Desktop')
# >>> for textFilePathObj in p.glob('*.txt'):
# ...     print(textFilePathObj) # Prints the Path object as a string.
# ...     # Do something with the text file.
# ...
# C:\Users\Al\Desktop\foo.txt
# C:\Users\Al\Desktop\spam.txt
# C:\Users\Al\Desktop\zzz.txt