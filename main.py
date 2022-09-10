import os

globalBoard = [
    ["A-P1", "A-P2", "A-P3", "A-P4", "A-P5"],
    ["A-H1", "-", "A-H3", "-", "-"],
    ["A-H2", "-", "-", "-", "-"],
    ["B-H1", "B-H3", "B-H2", "-", "-"],
    ["B-P1", "B-P2", "B-P3", "B-P4", "B-P5"]
]
currentChrarcters = {
    "A": ["P1", "P2", "P3", "P4", "P5", "H1", "H2", "H3"],
    "B": ["P1", "P2", "P3", "P4", "P5", "H1", "H2", "H3"]
}
legalMoves = {
    "P": ["L", "R", "U", "D"],
    "H1": ["L", "R", "U", "D"],
    "H2": ["FL", "FR", "BL", "BR"],
    "H3": ["FL", "FR", "BL", "BR", "RF", "RB", "LF", "LB"]
}





class Board():
    def __init__(self):
        pass


    def print_board(self):
        os.system('cls')
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
        locI = 0
        locJ = 0
        for i in range(len(globalBoard)):
            for j, ele in enumerate(globalBoard[i]):
                if turn + "-" + character == ele:
                    locI = i
                    locJ = j


        if character[0] == "P":
            newLocI, newLocJ = pieces.movePawn(locI, locJ, move)
        elif character == "H1":
            newLocI1, newLocJ1, newLocI, newLocJ = pieces.moveH1(locI, locJ, move)
        elif character == "H2":
            newLocI1, newLocJ1, newLocI, newLocJ = pieces.moveH2(locI, locJ, move)
        elif character == "H3":
            newLocI, newLocJ = pieces.moveH3(locI, locJ, move)


        defaultMove = True
        if (newLocI < 0 or newLocI > 4) or (newLocJ < 0 or newLocJ > 4):
            defaultMove = False
            print("Error: Cannot Move Here")
            return 0

        if character[0] == "P":
            if(globalBoard[newLocI][newLocJ].split("-")[0] == turn):
                defaultMove = False
                print("Error: Hitting own Player")
                return 0
        elif character == "H1" or character == "H2":
            if(globalBoard[newLocI1][newLocJ1].split("-")[0] == turn) or (globalBoard[newLocI][newLocJ].split("-")[0] == turn):
                defaultMove = False
                print("Error: Hitting own Player on the way.")
                return 0
        if character[0] == "P":
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
        
        
        if(len(currentChrarcters["A"]) == 0):
            print("B won the game!")
            return 1
        if(len(currentChrarcters["B"]) == 0):
            print("A won the game!")
            return 1

class Pieces():
    def __init__(self) -> None:
        pass
    def processInput(self, inpt):
        [turn, character, move] = inpt.split("-")
        if character not in currentChrarcters[turn]:
            print("Error: Invalid Character input")
            return 0
        characterType = character
        if character[0] == "P":
            characterType = "P"
        if move not in legalMoves[characterType]:
            print("Error: Invalid Move by character")
            return 0
        return [turn, character, move]
    def movePawn(self, locI, locJ, move):
        newLocI = locI
        newLocJ = locJ
        if move == "L":
            newLocJ -= 1
        elif move == "R":
            newLocJ += 1
        elif move == "U":
            newLocI -= 1
        elif move == "D":
            newLocI += 1
        else:
            print("Error: Wrong Move")
            return 0
        return newLocI, newLocJ
    
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
        elif move == "U":
            newLocI1 -= 1
            newLocI2 -= 2
        elif move == "D":
            newLocI1 += 1
            newLocI2 += 2
        else:
            print("Error: Wrong Move")
            return 0
        return newLocI1, newLocJ1, newLocI2, newLocJ2
    
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
    board.print_board()
    finalMove = ""
    if turn == False:
        to = input("Where do you wanna move which piece player A: ")
        finalMove = "A-" + to
    elif turn == True:
        to = input("Where do you wanna move which piece player B: ")
        finalMove = "B-" + to


    parsedInp = pieces.processInput(finalMove)
    if parsedInp == 0:
        input("Press any character to retry")
        continue

    result = board.movePiece(parsedInp)
    if result == 0:
        input("Press any character to retry")
        continue
    elif result == 1:
        input("Press any character to exit!")
        break

    turn = not turn
