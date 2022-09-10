import os
from turtle import clearscreen

globalBoard = [
    ["A-P1", "A-P2", "A-P3", "A-P4", "A-P5"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["B-P1", "B-P2", "B-P3", "B-P4", "B-P5"]
]
currentChrarcters = {
    "A": ["P1", "P2", "P3", "P4", "P5"],
    "B": ["P1", "P2", "P3", "P4", "P5"]
}
legalMoves = {
    "P": ["L", "R", "U", "D"]
}





class Board():
    """
    Put description of the Board class here
    """
    def __init__(self):
        # replace body with the initialization of a standard
        # chess board with it's pieces placed correctly
        pass

    def clearScreen(self):
        os.system('cls')
    def print_board(self):
        # replace body with how you want your board printed
        os.system('cls')
        for i in range(len(globalBoard)):
            for j in globalBoard[i]:
                if(j == "-"):
                    print("    " + j + "  ", end="")
                else:
                    print("  "+j, end = " ")
            print()
        pass
    def movePiece(self, parsedInp):
        [turn, character, move] = parsedInp
        locI = 0
        locJ = 0
        for i in range(len(globalBoard)):
            for j, ele in enumerate(globalBoard[i]):
                if turn + "-" + character == ele:
                    locI = int(i)
                    locJ = int(j)
        newLocI = locI
        newLocJ = locJ
        if character[0] == "P":
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
        if (newLocI < 0 or newLocI > 4) or (newLocJ < 0 or newLocJ > 4):
            print("Error: Cannot Move Here")
            return 0
        if(globalBoard[newLocI][newLocJ].split("-")[0] == turn):
            print("Error: Hitting own Player")
            return 0
        if(globalBoard[newLocI][newLocJ] != "-") and (globalBoard[newLocI][newLocJ].split("-")[0] != turn):
            currentChrarcters[globalBoard[newLocI][newLocJ].split("-")[0]].remove(globalBoard[newLocI][newLocJ].split("-")[1])
            globalBoard[locI][locJ] = "-"
            globalBoard[newLocI][newLocJ] = turn + "-" + character
            if(len(currentChrarcters["A"]) == 0):
                print("B won the game!")
                return 1
            if(len(currentChrarcters["B"]) == 0):
                print("A won the game!")
                return 1
        else:
            globalBoard[locI][locJ] = "-"
            globalBoard[newLocI][newLocJ] = turn + "-" + character

class Pieces():
    def __init__(self) -> None:
        pass
    def processInput(self, inpt):
        [turn, character, move] = inpt.split("-")
        if character not in currentChrarcters[turn]:
            print("Error: Invalid Character input")
            return 0
        characterType = character[0]
        if move not in legalMoves[characterType]:
            print("Error: Invalid Move by character")
            return 0
        return [turn, character, move]
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
