
import turtle
import tictactoeai
# Configure these variables as you like (within reason).
radius = 100
padding = 10
user = "O"

# These variables are then automatically configured.
if user == "O":
	ai = "X"
else:
	ai = "O"
numMoves = 0
stillPlaying = True
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def drawBoard():
	'''Draws an empty board. Each cell is a square of side length 2 * (radius + padding).'''
	global radius
	global padding
	size = radius + padding
	turtle.penup()
	turtle.setposition(-size, -3 * size)
	turtle.pendown()
	turtle.setposition(-size, 3 * size)
	turtle.penup()
	turtle.setposition(size, -3 * size)
	turtle.pendown()
	turtle.setposition(size, 3 * size)
	turtle.penup()
	turtle.setposition(-3 * size, -size)
	turtle.pendown()
	turtle.setposition(3 * size, -size)
	turtle.penup()
	turtle.setposition(-3 * size, size)
	turtle.pendown()
	turtle.setposition(3 * size, size)

def drawO(row, col):
	'''Draws an O in the given row and column.'''
	global radius
	global padding
	size = radius + padding
	x = -2 * size + col * 2 * size
	y = -2 * size + (2 - row) * 2 * size
	turtle.penup()
	turtle.setposition(x + radius, y)
	turtle.setheading(90)
	turtle.pendown()
	turtle.circle(radius)

def drawX(row, col):
	'''Draws an X in the given row and column.'''
	global radius
	global padding
	size = radius + padding
	x = -2 * size + col * 2 * size
	y = -2 * size + (2 - row) * 2 * size
	turtle.penup()
	turtle.setposition(x - radius, y - radius)
	turtle.pendown()
	turtle.setposition(x + radius, y + radius)
	turtle.penup()
	turtle.setposition(x - radius, y + radius)
	turtle.pendown()
	turtle.setposition(x + radius, y - radius)

def handleClick(x, y):
	'''This function is called whenever the user clicks in the turtle window with the mouse. It is passed the (x, y) coordinates of the mouse click. The origin is in the middle of the window, x increases to the right, and y increases up. This function interprets the mouse click as a user move, and then lets the AI move, if appropriate.'''
	global radius
	global padding
	global board
	global stillPlaying
	global numMoves
	size = radius + padding
	# Convert (x, y) into (row, col).
	if y < -size:
		row = 2
	elif y > size:
		row = 0
	else:
		row = 1
	if x < -size:
		col = 0
	elif x > size:
		col = 2
	else:
		col = 1
	if stillPlaying and board[row][col] == " ":
		# Interpret this click as a user move.
		numMoves += 1
		board[row][col] = user
		if user == "O":
			drawO(row, col)
		else:
			drawX(row, col)
		if tictactoeai.hasWon(board, user) or numMoves == 9:
			stillPlaying = False
		else:
			# Let the AI take its move.
			move = tictactoeai.aiMove(board, ai)
			numMoves += 1
			board[move[0]][move[1]] = ai
			if ai == "O":
				drawO(move[0], move[1])
			else:
				drawX(move[0], move[1])
			if tictactoeai.hasWon(board, ai) or numMoves == 9:
				stillPlaying = False

def main():
	# Initialize the turtle and the drawing canvas.
	turtle.hideturtle()
	turtle.speed(0)
	drawBoard()
	# Register functions to respond to user events --- in this case, just one.
	screen = turtle.getscreen()
	screen.onclick(handleClick)
	# Every interactive turtle program ends by entering the main loop.
	# All subsequent action occurs in event handlers such as handleClick.
	screen.mainloop()

if __name__ == "__main__":
	main()

