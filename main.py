import os
from colorama import Fore, Back, Style


globalBoard = [
    ["A-P1", "A-P2", "A-P3", "A-P4", "A-P5"],
    ["A-H1", "-", "A-H3", "-", "-"],
    ["A-H2", "-", "-", "-", "-"],
    ["B-H1", "B-H3", "B-H2", "-", "-"],
    ["B-P1", "B-P2", "B-P3", "B-P4", "B-P5"]
] #Game Board
currentChrarcters = {
    "A": ["P1", "P2", "P3", "P4", "P5", "H1", "H2", "H3"],
    "B": ["P1", "P2", "P3", "P4", "P5", "H1", "H2", "H3"]
} #Current Characters on the board
legalMoves = {
    "P": ["L", "R", "F", "B"],
    "H1": ["L", "R", "F", "B"],
    "H2": ["FL", "FR", "BL", "BR"],
    "H3": ["FL", "FR", "BL", "BR", "RF", "RB", "LF", "LB"]
} #List of legal moves per character



class Board():
    def __init__(self):
        pass

    def clearScreen(self):
        print(Style.RESET_ALL)
        os.system('cls')

    def print_board(self):
        self.clearScreen()
        for i in range(len(globalBoard)):
            for j in globalBoard[i]:
                if(j == "-"):
                    print("    " + j + "  ", end="")
                else:
                    print("  "+j, end = " ")
            print("\n")
        pass
    
    
    def movePiece(self, parsedInp):
        [turn, character, move] = parsedInp

        #Finding the location of the piece to move
        locI = 0
        locJ = 0
        for i in range(len(globalBoard)):
            for j, ele in enumerate(globalBoard[i]):
                if turn + "-" + character == ele:
                    locI = i
                    locJ = j

        #Calculating the final and intermediate steps of the respective piece
        if character[0] == "P":
            newLocI, newLocJ = pieces.movePawn(locI, locJ, move)
        elif character == "H1":
            newLocI1, newLocJ1, newLocI, newLocJ = pieces.moveH1(locI, locJ, move)
        elif character == "H2":
            newLocI1, newLocJ1, newLocI, newLocJ = pieces.moveH2(locI, locJ, move)
        elif character == "H3":
            newLocI, newLocJ = pieces.moveH3(locI, locJ, move)


        #Edge Case Testing
        defaultMove = True #Flag for default case
        if (newLocI < 0 or newLocI > 4) or (newLocJ < 0 or newLocJ > 4):
            defaultMove = False
            print("Error: Cannot Move Here") #Moving Out of bounds
            return 0


        if character[0] == "P":
            if(globalBoard[newLocI][newLocJ].split("-")[0] == turn):
                defaultMove = False
                print("Error: Hitting own Player") #Hitting own Player
                return 0
        elif character == "H1" or character == "H2":
            if(globalBoard[newLocI1][newLocJ1].split("-")[0] == turn) or (globalBoard[newLocI][newLocJ].split("-")[0] == turn):
                defaultMove = False
                print("Error: Hitting own Player on the way.") #Hitting own player or own player in the way
                return 0
        
        #Collision detection based on the character
        if character[0] == "P" or character == "H3":
            if(globalBoard[newLocI][newLocJ] != "-") and (globalBoard[newLocI][newLocJ].split("-")[0] != turn):
                currentChrarcters[globalBoard[newLocI][newLocJ].split("-")[0]].remove(globalBoard[newLocI][newLocJ].split("-")[1])
                globalBoard[locI][locJ] = "-"
                globalBoard[newLocI][newLocJ] = turn + "-" + character
                defaultMove = False
        elif character == "H1" or character == "H2":
            globalBoard[locI][locJ] = "-"
            if(globalBoard[newLocI1][newLocJ1] != "-") and (globalBoard[newLocI1][newLocJ1].split("-")[0] != turn):
                currentChrarcters[globalBoard[newLocI1][newLocJ1].split("-")[0]].remove(globalBoard[newLocI1][newLocJ1].split("-")[1])
                globalBoard[newLocI1][newLocJ1] = "-"
                defaultMove = False
            if(globalBoard[newLocI][newLocJ] != "-") and (globalBoard[newLocI][newLocJ].split("-")[0] != turn):
                currentChrarcters[globalBoard[newLocI][newLocJ].split("-")[0]].remove(globalBoard[newLocI][newLocJ].split("-")[1])
                defaultMove = False
            
            globalBoard[newLocI][newLocJ] = turn + "-" + character
        if defaultMove:    
            globalBoard[locI][locJ] = "-"
            globalBoard[newLocI][newLocJ] = turn + "-" + character
        
    
    def checkWon(self):
        if(len(currentChrarcters["A"]) == 0):
            print("B won the game!")
            return 1
        if(len(currentChrarcters["B"]) == 0):
            print("A won the game!")
            return 1

class Pieces():
    
    def __init__(self) -> None:
        pass
    # Parsing the input
    def processInput(self, inpt):
        [turn, character, move] = inpt.split("-")
        if character not in currentChrarcters[turn]:            # Checking whether the character is on the board or not
            print("Error: Invalid Character input")
            return 0
        
        characterType = character
        if character[0] == "P":
            characterType = "P"
        
        if move not in legalMoves[characterType]:      #Checking whether the move is legal or not
            print("Error: Invalid Move by character")
            return 0
        return [turn, character, move]

    #Handling Pawn Movement
    def movePawn(self, locI, locJ, move):
        newLocI = locI
        newLocJ = locJ
        if move == "L":
            newLocJ -= 1
        elif move == "R":
            newLocJ += 1
        elif move == "F":
            newLocI -= 1
        elif move == "B":
            newLocI += 1
        else:
            print("Error: Wrong Move")
            return 0
        return newLocI, newLocJ
    
    #Handling H1 Movement
    def moveH1(self, locI, locJ, move):
        newLocI1 = locI
        newLocJ1 = locJ
        newLocI2 = locI
        newLocJ2 = locJ
        if move == "L":
            newLocJ1 -= 1
            newLocJ2 -= 2
        elif move == "R":
            newLocJ1 += 1
            newLocJ2 += 2
        elif move == "F":
            newLocI1 -= 1
            newLocI2 -= 2
        elif move == "B":
            newLocI1 += 1
            newLocI2 += 2
        else:
            print("Error: Wrong Move")
            return 0
        return newLocI1, newLocJ1, newLocI2, newLocJ2
    
    #Handling H2 Movement
    def moveH2(self, locI, locJ, move):
        newLocI1 = locI
        newLocJ1 = locJ
        newLocI2 = locI
        newLocJ2 = locJ
        if move == "FL":
            newLocJ1 -= 1
            newLocI1 -= 1
            newLocJ2 -= 2
            newLocI2 -= 2
        elif move == "FR":
            newLocJ1 += 1
            newLocI1 -= 1
            newLocJ2 += 2
            newLocI2 -= 2
        elif move == "BL":
            newLocJ1 -= 1
            newLocI1 += 1
            newLocJ2 -= 2
            newLocI2 += 2
        elif move == "BR":
            newLocJ1 += 1
            newLocI1 += 1
            newLocJ2 += 2
            newLocI2 += 2
        else:
            print("Error: Wrong Move")
            return 0
        return newLocI1, newLocJ1, newLocI2, newLocJ2
    
    #Handling H3 Movement
    def moveH3(self, locI, locJ, move):
        newLocI = locI
        newLocJ = locJ
        if move == "FL":
            newLocJ -= 1
            newLocI -= 2
        elif move == "FR":
            newLocJ += 1
            newLocI -= 2
        elif move == "BR":
            newLocJ += 1
            newLocI += 2
        elif move == "BL":
            newLocJ -= 1
            newLocI += 2
        elif move == "RF":
            newLocJ += 2
            newLocI -= 1
        elif move == "RB":
            newLocJ += 2
            newLocI += 1
        elif move == "LF":
            newLocJ -= 2
            newLocI -= 1
        elif move == "LB":
            newLocJ -= 2
            newLocI += 1
        else:
            print("Error: Wrong Move")
            return 0
        return newLocI, newLocJ



turn = False
board = Board()
pieces = Pieces()
while 1:
    board.print_board() #Printing Board
    if(board.checkWon() == 1): #Checking whether anyone won.
        input("Press any character to exit!")
        break
    finalMove = ""
    if turn == False:
        to = input("Where do you wanna move which piece" + Fore.RED + " player A(Eg. P5-B): ")
        finalMove = "A-" + to
    elif turn == True:
        to = input("Where do you wanna move which piece" + Fore.GREEN + " player B(Eg. P5-F): ")
        finalMove = "B-" + to


    parsedInp = pieces.processInput(finalMove)
    if parsedInp == 0: #Error Case
        input("Press any character to retry")
        continue

    result = board.movePiece(parsedInp)
    if result == 0: #Error Case
        input("Press any character to retry")
        continue

    turn = not turn
