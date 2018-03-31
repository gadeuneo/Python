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
def aiMove(b,p):
available = possibleMoves(b)
    # Check computer win moves
    for i in available(0, 9):
        if b[i] == ' ' and testWinMove(b, p, i):
            return i
    # Check player win moves
    for i in available(0, 9):
        if b[i] == ' ' and testWinMove(b, p, i):
            return i
    # Check computer fork opportunities
    for i in available(0, 9):
        if b[i] == ' ' and testForkMove(b, p, i):
            return i
    # Check player fork opportunities, incl. two forks
    playerForks = 0
    for i in available(0, 9):
        if b[i] == ' ' and testForkMove(b, p, i):
            playerForks += 1
            tempMove = i
    if playerForks == 1:
        return tempMove
    elif playerForks == 2:
        for j in [1, 3, 5, 7]:
            if b[j] == ' ':
                return j
    # Play center
    if b[4] == ' ':
        return 4
    # Play a corner
    for i in [0, 2, 6, 8]:
        if b[i] == ' ':
            return i
    #Play a side
    for i in [1, 3, 5, 7]:
        if b[i] == ' ':
            return i
			
def testForkMove(b, mark, i):
    # Determines if a move opens up a fork
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    winningMoves = 0
    for j in range(0, 9):
        if testWinMove(bCopy, mark, j) and bCopy[j] == ' ':
            winningMoves += 1
    return winningMoves >= 2
	
def getBoardCopy(b):
    # Make a duplicate of the board. When testing moves we don't want to 
    # change the actual board
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard

def testWinMove(b, mark, i):
    # b = the board
    # mark = 0 or X
    # i = the square to check if makes a win 
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    return checkWin(bCopy, mark)