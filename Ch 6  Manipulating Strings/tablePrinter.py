#! python3

""" Prints a given table into formatted columns
    Arguments:  List of Lists
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

# print('The length of x is ' + str(len(tableData[0])))
# print('The length of y is ' + str(len(tableData)))
# print('The length of tableData is ' + str(len(tableData)))

def printTable(table):

    colwidths = [0] * len(table)
    for i in range(len(table)):  # loops through the tables and get the max string length to put into colwidths list
        for x in table[i]:
            if len(x) > colwidths[i]:
                colwidths[i] = len(x)

    for y in range(len(table[0])):
        for x in range(len(table)):
 #           colwidths[x] = len(max(table[x], key=len))  # this is an alternate way of doing it with max
            print(table[x][y].rjust(colwidths[x]), end=' ')
        print()


printTable(tableData)
