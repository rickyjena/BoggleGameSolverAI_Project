__author__ = 'Saurabh Jena'

"""
Note: Please use this file with boggleSolverAIMain.py and also read the ReadMe
File. Also run the boggleSolverAIMain with the given interpreter.py file. I will
talk about this more in the Readme file.
"""

# These are global list datastructures that other functions wil reference to
myDict = []
myBoard = []

""" 
loadDictionary(inputDict): This function is a helper function I have created to
load our dictionary into a list datastructure to reference to. This takes in a
input dictionary textfile or a list of words of any language then turns it into
a list that the the other functions can make a comparision to.
"""
def loadDictionary(inputDict):
    global myDict
    inputDictFile = open( inputDict,'r')
    for line in inputDictFile:
        myDict.append(line.strip('\n'))
    inputDictFile.close()
    print("Dictionary data has been stored")
    return

"""
loadBoard(inputFile): This function was made to open the the board.txt file and
store the board in a list type data structure so it could be used in other
functions.
"""
def loadBoard(inputFile):
    global myBoard
    inputData = open( inputFile,'r')
    for line in inputData:
        myBoard.append(line.strip('\n').replace(" ",""))
    inputData.close()
    print("Boards data has been stored")
    return

"""
printBoard(inputBoard): This function prints out the the board that the AI will
be playing boggle on and be getting data from.
"""
def printBoard(inputBoard):
    maxSizeOfBoard = len(inputBoard[0])
    for i in range(0,maxSizeOfBoard):
        for j in range(0,maxSizeOfBoard):
            print(inputBoard[i][j]+" ",end="")
        print()
    return

"""
possibleMoves(coordinates,inputBoard):This function will go through the board
and find all the possible moves you can go to from point that is inputed as a
parameter in the function.
"""
def possibleMoves(coordinates,inputBoard):
    maxSizeOfBoard = len(inputBoard[0])
    possibleMovesSet = []
    #indexes for coordinates in matrix
    i = int(coordinates[0])
    j = int(coordinates[1])

    #Here are the conditionals for each surrounding spot
    #(i-1,j)
    if (i-1)>=0:
        possibleMovesSet.append((i-1,j))
    #(i+1,j)
    if (i+1)<maxSizeOfBoard:
        possibleMovesSet.append((i+1,j))
    #(i-1,j+1)
    if ((i-1)>=0 and (j+1)<maxSizeOfBoard):
        possibleMovesSet.append((i-1,j+1))
    #(i+1,j+1)
    if ((i+1)<maxSizeOfBoard and (j+1)<maxSizeOfBoard):
        possibleMovesSet.append((i+1,j+1))
    #(i+1,j-1)
    if ((i+1)<maxSizeOfBoard and (j-1)>=0):
        possibleMovesSet.append((i+1,j-1))
    #(i,j-1)
    if (j-1)>=0:
        possibleMovesSet.append((i,j-1))
    #(i,j+1)
    if (j+1)<maxSizeOfBoard:
        possibleMovesSet.append((i,j+1))
    #(i-1,j-1)
    if ((i-1)>=0 and (j-1)>=0):
        possibleMovesSet.append((i-1,j-1))
    return set(possibleMovesSet)

"""
legalMoves( possibleMovesFunct, usedMoves ):This function will take in the
possibleMovesFunct to get a set of all the possible moves. Then the next
parameter will be the moves that you have already gone through. After that it
will remove the used moves from the set of possible moves and return the set of
legal moves.
"""
def legalMoves( possibleMovesFunct, usedMoves ):
    listOfPos = list(possibleMovesFunct)
    listOfUsed = list(usedMoves)
    listOfLegal = [i for i in listOfPos if i not in listOfPos 
        or i not in listOfUsed]
    return set(listOfLegal)

"""
examineState(inputBoard, currentloc, listOfMoves, inputDictionary):This function
takes in the game board, your current location on the board, a list of moves you
are taking, and the dictionary we made from loadDictionary. So basically after
taking in these parameters the function ends up examining the board, looking at
the list of moves you gave it, and ends up comparing it with the the words given
in the dictionary to see if yes that word exist or not.
"""
def examineState(inputBoard, currentloc, listOfMoves, inputDictionary):
    wordLetterList = []
    word =''
    result = ()
    numOfLisOfMov = len(listOfMoves)
    #loops through list of moves and adds letter to list from coordinates
    for i in range(0,numOfLisOfMov):
        wordLetterList.append(myBoard[listOfMoves[i][0]][listOfMoves[i][1]])
    
    #adds the currentLoc letter to end of the list
    wordLetterList.append(myBoard[currentloc[0]][currentloc[1]])
    
    #loops through the word letter list and makes a word out of it
    for j in wordLetterList:
        word += j
    
    #conditionals for checking if the word exists
    if word.lower() in inputDictionary:
        result = result + (word.lower(),) + ('Yes',)
    else:
        result = result + (word.lower(),) + ('No',)
    
    #returns the result
    return result

"""
loadDictionary('twl06.txt')
loadBoard('fourboard3.txt')
printBoard(myBoard)
possibleMoves((3,3),myBoard)
possibleMoves((2,1),myBoard)
legalMoves(possibleMoves((1,2),myBoard), ((1,0),(2,0),(2,1),(2,2)))
legalMoves(possibleMoves((2,2),myBoard), ((1,1),(1,2),(1,3),(2,3),(3,2)))
examineState(myBoard,(0,3),((1,1),(0,1),(0,2)), myDict)
examineState(myBoard, (0,0), ((3,3),(2,2),(1,1)), myDict)
examineState(myBoard,(3,3),((2,2),(2,1),(2,0),(3,0),(3,1),(3,2)), myDict)
"""
"""
loadDictionary('twl06.txt')
loadBoard('fourboard3.txt')
printBoard(myBoard)
possibleMoves((0,0), myBoard)
possibleMoves((2,2), myBoard)
legalMoves( possibleMoves((2,2),myBoard), ((0,0),(1,1),(2,2),(3,3)) )
examineState(myBoard,(0,0),((1,1),(1,0)), myDict)
examineState(myBoard, (1,0), ((2,2),(2,1),(1,1)), myDict)
examineState(myBoard,(3,1),((0,1),(1,0),(1,1),(2,1)), myDict)
"""