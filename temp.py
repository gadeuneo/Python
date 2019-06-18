import sys
import random
import copy

class Board:
    def __init__(self, squareLst, index):
        self.sqrLst = squareLst
        self.value = " "
        self.index = index

    def setValue(self, value):
        self.value = value
    
    def getValue(self):
        return self.value

    def getSquares(self):
        return self.sqrLst

class Square:
    def __init__(self, index):
        self.value = " "
        self.index = index

    def setValue(self, Value):
        self.value = Value

    def getValue(self):
        return self.value


'''
    Checks win on a board
    board = [0, 1, 2
            3, 4, 5
            6, 7, 8]
'''

def checkWin(board, player):
    if (board[0].getValue() == board[1].getValue() == board[2].getValue() and board[0].getValue() == player):
        return True
    elif (board[3].getValue() == board[4].getValue() == board[5].getValue() and board[3].getValue() == player):
        return True
    elif (board[6].getValue() == board[7].getValue() == board[8].getValue() and board[6].getValue() == player):
        return True
    elif (board[0].getValue() == board[3].getValue() == board[6].getValue() and board[0].getValue() == player):
        return True
    elif (board[1].getValue() == board[4].getValue() == board[7].getValue() and board[1].getValue() == player):
        return True
    elif (board[2].getValue() == board[5].getValue() == board[8].getValue() and board[2].getValue() == player):
        return True
    elif (board[0].getValue() == board[4].getValue() == board[8].getValue() and board[0].getValue() == player):
        return True
    elif (board[6].getValue() == board[4].getValue() == board[2].getValue() and board[2].getValue() == player):
        return True
    else:
        return False


def display(board):
    #print top row
    print(" " + board[0].getValue() + "|" + board[1].getValue() + "|" + board[2].getValue())
    #print middle row
    print(" " + board[3].getValue() + "|" + board[4].getValue() + "|" + board[5].getValue())
    #print bottom row
    print(" " + board[6].getValue() + "|" + board[7].getValue() + "|" + board[8].getValue())

def showChoice(open):
    clear = [0,1,2,
            3,4,5,
            6,7,8]
    
    free = list(set(open).intersection(set(clear)))
    for i in range(len(clear)):
        if (i % 3 == 0):
            print("")
        if (i in [0, 3, 6]):
            print(" ", end='')
        if (i in free and i not in [2, 5, 8]):
            print(str(i) + "|", end='')
        elif(i in free and i in [2, 5, 8]):
            print(str(i), end='')
        elif(i not in free and i not in [2, 5, 8]):
            print(" |", end='')
        elif(i not in free and i in [2, 5, 8]):
            print(" ", end='')
    print("")

def playerChoice(board):
    open = []
    for i in range(len(board)):
        if (board[i].getValue() == " "):
            open.append(i)
    
    return open

def opponentAI(board, open):
    reset = copy.deepcopy(board)
    test = copy.deepcopy(board)
    move = []

    # Check for win
    for mini in range(len(open)):
        free = playerChoice(reset[mini].getSquares())
        for turn in free:
            test[mini].getSquares()[turn].setValue("O")
            if (checkWin(test[mini].getSquares(), "O")):
                move.append(mini)
                move.append(turn)
                return move
            else:
                test = copy.deepcopy(reset)
    # Check for opponent win
    for mini in range(len(open)):
        free = playerChoice(copy.deepcopy(board[mini].getSquares()))
        for turn in free:
            test[mini].getSquares()[turn].setValue("X")
            if (checkWin(test, "X")):
                move.append(mini)
                move.append(turn)
                return move
            else:
                test = copy.deepcopy(reset)
    # Random
    move.append(random.choice(open))
    move.append(random.choice(playerChoice(board[move[0]].getSquares())))
    return move



    # # Check win cond for turn
    # for turn in open:
    #     test[turn].setValue("O")
    #     if (checkWin(test, "O")):
    #         move = turn
    #         break
    #     else:
    #         test = copy.deepcopy(reset)
    # if (move != ''):
    #     return move
    # # Check opponent wind cond to block
    # for turn in open:
    #     test[turn].setValue("X")
    #     if (checkWin(test, "X")):
    #         move = turn
    #         break
    #     else:
    #         test = copy.deepcopy(reset)
    # if (move != ''):
    #     return move
    # # Random
    # return random.choice(open)

def makeBoard():
    board = []
    squares = []
    # initializes big board of boards
    for i in range(9):
        for j in range(9):
            for k in range(9):
                tempList = Square(k)
                squares.append(tempList)
            tempBoard = Board(squares, j)
            squares = []
        board.append(tempBoard)
        tempBoard = []

    return board

def main():

    master = makeBoard()

    display(master)
    print("Choices: ", end='')
    open = playerChoice(master)
    showChoice(open)

    turn = 0
    chosen = False
    valid = False
    while(turn < 81):

        while (not valid):
            choice = input("Choose a miniboard from choices: ")

            try:
                player = int(choice)
            except:
                continue

            if (player not in open):
                choice = input("Miniboard already assigned, choose again: ")
            else:
                mini = playerChoice(master[player].getSquares())
                display(master[player].getSquares())
                print("Choices: ", end='')
                showChoice(mini)
                while (not chosen):
                    next = input("Choose a point from valid choices: ")
                    try:
                        place = int(next)
                    except:
                        continue
                    
                    if (place not in mini):
                        next = input("Invalid choice, choose again: ")
                    else:
                        master[player].getSquares()[place].setValue("X")
                        valid = not valid
                        chosen = not chosen
        chosen = not chosen
        
        for i in range(len(master)):
            if (checkWin(master[i].getSquares(), "X")):
                master[i].setValue("X")
            elif (checkWin(master[i].getSquares(), "O")):
                master[i].setValue("O")
            elif (checkWin(master[i].getSquares(), "T")):
                master[i].setValue("T")

        if (checkWin(master, "X")):
            display(master)
            print("PLAYER WINS")
            sys.exit(0)
        
        opponentOpen = playerChoice(master)
        if (opponentOpen == []):
            print("TIE")
            sys.exit(0)

        #opponentChoice = random.choice(opponentOpen)
        opponentChoice = opponentAI(master, opponentOpen)
        master[opponentChoice[0]].getSquares()[opponentChoice[1]].setValue("O")
        # master[opponentChoice].setValue("O")
        if (checkWin(master, "O")):
            display(master)
            print("COMPUTER WINS")
            sys.exit(0)


        display(master)
        print("Choices for miniboards: ", end='')
        open = playerChoice(master)
        showChoice(open)
        valid = not valid
        

if __name__ == "__main__":
    main()