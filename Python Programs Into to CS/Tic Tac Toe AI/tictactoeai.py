import random

def hasWon(b, p):
	'''Returns a Boolean indicating whether player p has won on board b.'''
	return p == b[0][0] == b[0][1] == b[0][2] or p == b[1][0] == b[1][1] == b[1][2] or p == b[2][0] == b[2][1] == b[2][2] or p == b[0][0] == b[1][0] == b[2][0] or p == b[0][1] == b[1][1] == b[2][1] or p == b[0][2] == b[1][2] == b[2][2] or p == b[0][0] == b[1][1] == b[2][2] or p == b[0][2] == b[1][1] == b[2][0]

def possibleMoves(b):
	'''Returns a list of all available moves. The length is between 0 and 9, inclusively. (A move is a pair of integers, each between 0 and 2, inclusively.)'''
	avail = []
	for row in range(3):
		for col in range(3):
			if b[row][col] == " ":
				avail = avail + [[row, col]]
	return avail

def notP(p):
	if p == "X":
		return "O"
	else:
		return "X"



def aiMove(b, p):
	'''Assumes the board is not full. Returns a valid move for player p. (A move is a pair of integers, each between 0 and 2, inclusively.)'''
	
	available = possibleMoves(b)

	for move in available:
		print(b[move[0]][move[1]])
		b[move[0]][move[1]]=p
		if hasWon(b,p):
			return move
		else:
			b[move[0]][move[1]]=" "

	for move in available:
		print(b[move[0]][move[1]])
		b[move[0]][move[1]]=notP(p)
		if hasWon(b,notP(p)):
			return move
		else:
			b[move[0]][move[1]]=" "
			
	for i in available:
		if possibleMoves == " " and testMove(b,p):
			return i
	notPFork = 0
	for i in available:
		if possibleMoves == " " and testMove(b, p):
			notPFork += 1
			tempMove =i
	if notPFork == 1:
		return tempMove
	elif notPFork == 2:
		for j in available(side):
			if b[j] == " ":
				return j

	if b[1][1] == " ":
		return [1, 1]
		
	if corner == True:
		return corner
	if side == True:
		return side
	return available[random.randint(0, len(available) - 1)]

def aiNotP(b, notP):
	available = possibleMoves(b)

	for move in available:
		print(b[move[0]][move[1]])
		b[move[0]][move[1]]=notP(p)
		if hasWon(b,p):
			return move
		else:
			b[move[0]][move[1]]=" "

	for move in available:
		print(b[move[0]][move[1]])
		b[move[0]][move[1]]=notP(p)
		if hasWon(b,notP(p)):
			return move
		else:
			b[move[0]][move[1]]=" "
			
	for i in available:
		if b[i] == " " and testMove(b,p):
			return i
	notPFork = 0
	for i in available:
		if b[i] == " " and testMove(b, p):
			notPFork += 1
			tempMove =i
	if notPFork == 1:
		return tempMove
	elif notPFork == 2:
		for j in available(side):
			if b[j] == " ":
				return j

	if b[1][1] == " ":
		return [1, 1]
		
	if corner == True:
		return corner
	if side == True:
		return side

	return available[random.randint(0, len(available) - 1)]

def idFork(b, p):
	bCopy = futureBoard(b)
	bCopy[i] = p
	forkMove = 0
	for j in range(available):
		if testMove(bCopy, p) and bCopy[i] == " ":
			forkMove += 1
		return forkMove >= 2


def testMove(b, p):
    bCopy = futureBoard(b)
    bCopy[i] = p
    return checkWin(bCopy, p)
	
def futureBoard(b):
    dupeBoard = possibleMoves(b)
    for i in b:
        dupeBoard.append(i)
    return dupeBoard

def corner(b, p):
	if b[0][0] == " ":
		return [0,0]
	elif b[0][2] == " ":
		return [0,2]
	elif b[2][0] == " ":
		return [2,0]
	elif b[2][2] == " ":
		return [2,2]

def side(b,p):
	if b[0][1] == " ":
		return [0,1]
	elif b[1][0] == " ":
		return [1,0]
	elif b[1][2] == " ":
		return [1,2]
	elif b[2][1] == " ":
		return [2,1]
	
'''def main():
	b = [[" "," ", " "],
		[" "," ", " "],
		[" "," ", " "]]
	print(aiMove(b,"X"))
main()'''
	
