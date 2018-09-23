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


					

				
	return available[random.randint(0, len(available) - 1)]

			




def main():
	b = [[" "," ", " "],
		[" "," ", " "],
		[" "," ", " "]]
	print(aiMove(b,"X"))
main()
	
