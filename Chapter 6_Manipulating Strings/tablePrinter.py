#tablePrinter.py - A program that prints a table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def colWidthChecker():
    colWidth = []
    listNum = 0                                        #temp number that contains the number of the list we are working on, if it's list number 2, temp = 1, list number 10, temp = 9
    for listsInTableData in tableData:              #iterating over each list in tableData
        colWidth += [0]
        for values in listsInTableData:             #iterating over each value in those lists
            if len(values) > colWidth[listNum]:
                 colWidth[listNum] = len(values)
        listNum += 1

def printTable():
    return

colWidthChecker()