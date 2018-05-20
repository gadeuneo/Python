import tictactoeai

def userMove(b):
	'''Assumes that the board is not full. Returns a valid move, chosen by the user. (A move is a pair of integers, each between 0 and 2, inclusively.)'''
	while True:
		row = input("Enter a row: A, B, or C: ")
		col = input("Enter a column: A, B, or C: ")
		row = ord(row) - ord("A")
		col = ord(col) - ord("A")
		if 0 <= row < 3 and 0 <= col < 3 and b[row][col] == " ":
			return [row, col]
		else:
			print("Please pick an available cell on the board.")

def printBoard(b):
	'''Prints the given board in a pretty format.'''
	print()
	print("     A  B  C")
	print()
	print("A    " + b[0][0] + "  " + b[0][1] + "  " + b[0][2])
	print("B    " + b[1][0] + "  " + b[1][1] + "  " + b[1][2])
	print("C    " + b[2][0] + "  " + b[2][1] + "  " + b[2][2])

	printBoard(b)
	print("User, you are playing O. Choose your move.")
	while stillPlaying:
		numMoves += 1
		move = userMove(b)
		b[move[0]][move[1]] = "O"
		printBoard(b)
		if tictactoeai.hasWon(b, "O"):
			print("Congratulations. You win.")
			stillPlaying = False
		elif numMoves == 9:
			print("Like most tic-tac-toe games, it's a tie.")
			stillPlaying = False
		else:
			numMoves += 1
			move = tictactoeai.aiMove(b, "X")
			b[move[0]][move[1]] = "X"
			printBoard(b)
			if tictactoeai.hasWon(b, "X"):
				print("Bad news. You lose.")
				stillPlaying = False

if __name__ == "__main__":
	main()

