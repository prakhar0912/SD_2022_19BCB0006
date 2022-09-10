import os
from turtle import clearscreen

globalBoard = [
    ["A-P1", "A-P2", "A-P3", "A-P4", "A-P5"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["B-P1", "B-P2", "B-P3", "B-P4", "B-P5"]
]
currentChrarcters = ["P1", "P2", "P3", "P4", "P5"]
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
    def movePiece(parsedInp):
        [turn, character, move] = parsedInp
        for i in range(len(globalBoard)):
            for j in globalBoard[i]:
                if turn + "-" + character == j:
                    locI, locJ = i, j
        print(locI, locJ)



class Pieces():
    def __init__(self) -> None:
        pass
    def processInput(inpt):
        [turn, character, move] = inpt.split("-")
        if character not in currentChrarcters:
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
    if turn == False:
        to = input("Where do you wanna move which piece player A: ")
        finalMove = "A" + to
    elif turn == True:
        to = input("Where do you wanna move which piece player B: ")
        finalMove = "B" + to
    parsedInp = pieces.processInput(finalMove)
    if parsedInp == 0:
        input("Press any character to retry")
        continue
    board.movePiece(parsedInp)
    board.print_board()
    print(parsedInp)

    turn = not turn
