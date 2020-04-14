# James Gardner
#
# Challenger Number Newspaper Puzzle Solver
# 
#Fill in each square with a number, 1-9. Horizontal squares
#	should add to totals on the right. Vertical squares
#	should add to totals on the bottom. Diagonal squares
#	should add to totals in upper and lower right.
# There may be more than one solution
#
# Example
# 					|7
# 5	1	1	1	|8
# 3	2	2	1	|8
# 1	2	1	1	|5
# 2	4	1	2	|9
# --------------
# 11	9	5	5	10
# 
# Takes in a comma separated text file with numbers
# 	at the appropiate indices. Each index will correspond
# 	to a 'row' as it goes from top to bottom, left to right
# 	Outputs the solution.
#
# Example Text File: 
# 
# 23, 						[0]
# 1,0,0,0,28,				[1-5]
#	0,0,3,0,17,				[6-10]
# 0,0,0,3,10,				[11-15]
# 0,4,0,0,16,				[16-20]
# 15,24,18,14,11		[21-25]
 
import random
from time import *


if __name__ == '__main__':

	#initializes number list
	numList = [23,
	1,0,0,0,28,
	0,0,3,0,17,
	0,0,0,3,10,
	0,4,0,0,16,
	15,24,18,14,11]
	
	#checks number list for valid input
	for i in range(len(numList)):
		if numList[i] <0:
			print("Invalid input. Recheck all values.")
			break
	
	#creates row/column/diagonal list to check
	row1 = numList[1:6]
	row2 = numList[6:11]
	row3 = numList[11:16]
	row4 = numList[16:21]
	col1 = []
	col2 = []
	col3 = []
	col4 = []
	diagUp = []
	diagDown = []
	
	for i in range(len(numList)):
		if (i-1) % 5 == 0:
			col1.append(numList[i])
		elif (i-2) % 5 == 0:
			col2.append(numList[i])
		elif (i-3) % 5 == 0:
			col3.append(numList[i])
		elif (i-4) % 5 == 0:
			col4.append(numList[i])

	for i in range(len(numList)):
	#1,7,13,19,25
		if (i-1) % 6 == 0:
			diagUp.append(numList[i])
		elif (i % 4 ==0) and i < 17:
			diagDown.append(numList[i])
	diagDown.reverse()
	
	#temp lists for numbers that are allowed to be changed
	tempr1 = []
	tempr2 = []
	tempr3 = []
	tempr4 = []
	tempc1 = []
	tempc2 = []
	tempc3 = []
	tempc4 = []
	tempdu = []
	tempdd = []
	
	#temp lists
	row1t = row1
	row2t = row2
	row3t = row3
	row4t = row4
	
	
	#Sets numbers that are allowed to be changed
	
	#ROW 1
	for i in range(len(row1)):
			if row1[i] == 0:
				tempr1.append(False)
			else:
				tempr1.append(True)
	
	#ROW 2
	for i in range(len(row2)):
			if row2[i] == 0:
				tempr2.append(False)
			else:
				tempr2.append(True)
	
	#ROW 3
	for i in range(len(row1)):
			if row3[i] == 0:
				tempr3.append(False)
			else:
				tempr3.append(True)
	
	#ROW 4
	for i in range(len(row1)):
			if row4[i] == 0:
				tempr4.append(False)
			else:
				tempr4.append(True)
	
	
	while( (sum(row1[0:4]) != row1[4]) or (sum(row2[0:4]) != row2[4]) or (sum(row3[0:4]) != row3[4]) or (sum(row4[0:4]) != row4[4])):
	
		#Changes numbers until solution is found
		
		#ROW 1
		for i in range(len(row1)):
			if tempr1[i] == False:
				row1t.pop(i)
				row1t.insert(i,random.randint(1,9))
		
		#ROW 2
		for i in range(len(row2)):
			if tempr2[i] == False:
				row2t.pop(i)
				row2t.insert(i,random.randint(1,9))
		
		#ROW 3
		for i in range(len(row1)):
			if tempr3[i] == False:
				row3t.pop(i)
				row3t.insert(i,random.randint(1,9))
		
		#ROW 4
		for i in range(len(row1)):
			if tempr4[i] == False:
				row4t.pop(i)
				row4t.insert(i,random.randint(1,9))
	


