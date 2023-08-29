#! python 3
#! regexSearch.py - a program that scans .txt files in a specified folder for a user-supplied regex

import re
import pathlib
import os

#hardcoded path of the files which we wanna scan - obviously change the path if you want to scan other .txt files
myPath = pathlib.Path("G:\\Automate the boring stuff with Python\\Chapter 9 reading and writing files\\bunchOfTextFiles")
listOfTextFiles = []    #empty list - storing all the names of the .txt files found in that path

#loop that searches for text files in the specified path and adds that path to the empty list
i = 0
for textFile in myPath.glob('*.txt'):
    stringOfTextFilePath = ('\\'.join([str(myPath), str(textFile.name)]))
    p = pathlib.Path(stringOfTextFilePath)
    temp = p.read_text()
    print(temp)
    # os.startfile(listOfTextFiles[i])
    # i += 1



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