#tablePrinter.py - A program that prints a (transposed) table (it is transposed because it seems like this is the desired end result)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#function that determines the column width for later purposes
def colWidthChecker():
    colWidth = []
    listNum = 0                                        #temp number that contains the number of the list we are working on ()
    for listsInTableData in tableData:              #iterating over each list in tableData
        colWidth += [0]                             #initializing colWidth, filling the spot with 0 (length of each word has to be greater or equal to zero)
        for values in listsInTableData:             #iterating over each value in those lists
            if len(values) > colWidth[listNum]:
                 colWidth[listNum] = len(values)
        listNum += 1
    return colWidth

#function that transposes and prints the table
def printTable(columnData):
    #first: transposing the original table into the desired state (first column is now first row which we want to see first)
    transposedTable = []                                        #initializing empty transposed table
    for i in range(4):                                          #iterating over the length of columns from the original table (4 is a magic number in this case, it shouldn't be too complicated for this task, so we will leave it at that)
        transposedTable.append([column[i] for column in tableData])        
    #printing the transpoed table
    whichPosition = 0                                           #colWidth is a list which contains info on the max length of each initial row, 
    printedString = ""                                          #local string variable, each value of each row of the transposed table is saved in this string variable    
    for rowsInTable in transposedTable:
        for eachValue in rowsInTable:
            printedString = printedString + " " + eachValue.rjust(columnData[whichPosition])    #filling the string with each value and a whitespace in between, otherwise the longest value doesn't connect properly
            whichPosition += 1                                                                  #whichPosition starts at 0, ends at 2.
        print(printedString)
        whichPosition = 0                   #resetting whichPosition 
        printedString = ""                  #resetting printedString

myColumns = colWidthChecker()
printTable(myColumns)