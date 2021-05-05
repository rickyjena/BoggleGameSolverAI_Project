__author__ = 'Saurabh Jena'

import time

"""
Note: Please use this file with boggleSolverAIMain.py and also read the ReadMe
File. Also run the boggleSolverAIMain with the given interpreter.py file. I will
talk about this more in the Readme file.
"""

# These are global list datastructures that other functions wil reference to
myDict = []
myBoard = []
counter = 0

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
    #print("Boards data has been stored")
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
solveBoard(inputBoard,visited,currentLoc,inputWord,inputWordList):This function
is a recursive function that traverses through the board sets the location
visited if it has been visited and gets words that can be made through out the
board. Then it returns a list of all the words.
"""
def solveBoard(inputBoard,visited,currentLoc,inputWord,inputWordList):
    #We will us e this as a counter for the time this function runs
    global counter
    #Here we increment the counter
    counter+=1
    #Set cell to visited
    visited[currentLoc[0]][currentLoc[1]]= True
    #Add the cell to the input 
    inputWord = inputWord + myBoard[currentLoc[0]][currentLoc[1]]
    #Check if created word is in the dictionary
    if(inputWord.lower() in myDict):
        inputWordList.append(inputWord)
    #Store all the neighbors
    neighbors = list(possibleMoves(currentLoc,inputBoard))
    #loop through the neighbors
    for k in neighbors:
        #check if in bounds and not visted
        if( k[1]>=0 and k[0]>=0 and k[1]<=len(inputBoard) 
            and k[1]<=len(inputBoard) and not visited[k[0]][k[1]]):
            #recursivly call function on neighbors
            solveBoard(inputBoard,visited,k,inputWord,inputWordList)
    #add onto the word
    inputWord=""+inputWord[len(inputWord) -1]
    #reassign cells in visited matrix
    visited[currentLoc[0]][currentLoc[1]] = False
    #return the list of words
    return inputWordList

"""
def findWords(inputBoard):This function calls the recursive function on each
cell in the grid. We also end up timing how long it takes for the function to
run through and find all the posiible words.
"""
def findWords(inputBoard):
    #print statement to show that we have started looking for all the words
    print("And we're off!\n"+
    "Running with cleverness OFF\n")
    #This is starting time for when we start recursively finding words
    start = time.time()
    #string to store word in
    word = ""
    #the list to store the words
    wordList = []
    #get the max size for the board
    maxSizeOfBoard = len(myBoard)
    #This is a visited array to check if a cell has been visited or not
    visited = [[False for x in range(maxSizeOfBoard)]for y 
        in range(maxSizeOfBoard)]
    for i in range(0,maxSizeOfBoard):
        for j in range(0,maxSizeOfBoard):
            solveBoard(inputBoard,visited,(i,j),word,wordList)
    #This is the end time for our word search throughout the board
    end = time.time()
    #This is the total time taken to find the words.
    totalTime = end-start
    print("All Done\n")
    #print out the total moves searched through out the board 
    # and the time it took
    print("Searched total of "+ str(counter) + " moves in " + str(totalTime) 
        + " seconds\n")
    return wordList

"""
def runBoard(inputFileName):This function is like a main function that runs all
the functions contained in this file to get our desired output.
"""
def runBoard(inputFileName):
    #First we got to load in the board
    loadBoard(inputFileName)
    print('')
    #Then we got to print the board
    printBoard(myBoard)
    print('')
    #We store the total words found in a list
    totalWordList = findWords(myBoard)
    print("Words found:")
    #We splist our list of words into groups based on the length of the word
    dct = {}
    for elem in totalWordList:
        if len(elem) not in dct:
            dct[len(elem)] = [elem]
        elif len(elem) in dct: 
            dct[len(elem)] += [elem]
        result=[]
        for key in sorted(dct):
            result.append(dct[key])
    tempPrint = ""
    #We create this loop to print out the words based off of there length group
    for i in range(0,len(result)):
        tempList=result[i]
        tempPrint = ', '.join(str(elem) for elem in tempList)
        print(len(result[i][0]), " -letter words:",tempPrint)
    #We print the total number of words found
    print("\nFound ",len(totalWordList), " words in total.")
    #We print out the total list of words in alphabetical order
    print("Alpha-sorted list words:")
    totalWordList.sort()
    anothaTempPrint = ', '.join(str(elem) for elem in totalWordList)
    print(anothaTempPrint)
    return