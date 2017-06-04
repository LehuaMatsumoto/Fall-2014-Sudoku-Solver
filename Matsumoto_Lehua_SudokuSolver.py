#Lehua Matsumoto
#October 31, 2014

def readGrid(filename):
    f = open(filename)
    x = 0
    bigList = []
    while x < 9:
        rowText = f.readline()
        rowList = rowText.split() #no parameters - assumed to be a space
        for i in range(0, 9):
            rowList[i] = int(rowList[i])
        x = x + 1
        bigList = bigList + [rowList]
    return bigList

def printGrid(bigList):
    end = ""
    for i in bigList:
        for x in i:
            print x,
        print()

def boardChecker(bigList):
    h = correctRow(bigList)
    j = correctColumn(bigList)
    m = correctSubGrid(bigList)
    if h == False or j == False or m == False:
        #print("\nThis board is wrong.")
        return False
    if h == True and j == True and m == True:
        return True

def correctRow(bigList): #check row
    for i in bigList:
        l = i[:]
        #print("\nrow = ", end="")
        #print(l)
        l.sort()
        for x in range(0, 8):
            if l[x] == l[x+1] and l[x] != 0:
                #print("\nThere are two of the same numbers in one row.")
                return False
    return True
    
def correctColumn(bigList): #check column
    for k in range(0, 9):
        columnList = []
        for i in bigList:
            columnList.append(i[k])
        #print("\ncolumn = ", end="")
        #print(columnList)
        columnList.sort()
        for x in range(0, 8):
            if columnList[x] == columnList[x+1] and columnList[x] != 0: 
                #print("\nThere are two of the same numbers in one column.")
                return False
    return True

def correctSubGrid(bigList): #check subGrid
    for k in range(0, 9, 3):
        for m in range(0, 9, 3):
            subGrid = []
            for i in range(0, 3):
                for j in range(0, 3):
                    subGrid.append(bigList[i+m][j+k])
            #print("\nsubgrid = ", end="")
            #print(subGrid) 
            subGrid.sort()
            for x in range(0, 8):
                if subGrid[x] == subGrid[x+1] and subGrid[x] != 0: 
                    #print("\nThere are two of the same numbers in one subgrid.")
                    return False
    return True

def solve(bigList):
    x = findEmptySpace(bigList)
    if x == None:
        h = boardChecker(bigList)
        if h == False:
            #print("\nThis board is wrong.") 
            return False
        if h == True:
            print("\nCompleted board:\n")
            k = printGrid(bigList)
            return True
    else:
        row = x[0]
        col = x[1]
        while bigList[row][col] < 9:
            bigList[row][col] += 1
            #print("\nbigList[row][col] = "+str(bigList[row][col]))
            h = boardChecker(bigList)
            if h == True:
                #print("\nNext Attempt")
                #k = printGrid(bigList)
                j = solve(bigList)
                if j == True:
                    return True
        bigList[row][col]=0
        return False

def findEmptySpace(g):
    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col]==0:
                #print("\nrow = "+str(row)+" & col = "+str(col))
                return [row, col]
    
def main():
    print("Sudoku Board: \n")
    #Change 'sample.board' to whatever text file holds the empty sudoku board
    #Use '0's in place of empty spaces on the board
    grid = readGrid("sample.board") 
    x = printGrid(grid)
    #h = boardChecker(grid)
    j = solve(grid)
    print("\nYAY! Finished with the puzzle!")
    

main()
