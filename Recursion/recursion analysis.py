#James Gardner
import math
import turtle
import time


# Computes Paul's monologue length.
# Input: Positive integer n.
# Returns: Positive integer.
def monologueLength(n):
    if n ==1:
        return 1
    while n > 1:
        if n % 2==0:
            return monologueLength(n//2)+1
        else:
            return monologueLength(3*n+1)+1
            
# Computes the combination function n! / (k! (n - k)!).
# Input: Nonnegative integer n. Integer k such that 0 <= k <= n.
# Returns: Positive integer.
def choose(n,k):
    if n ==1 or n==k or k==0:
        return 1
    while k>0:
        return choose(n-1,k)+choose(n-1,k-1)


#Koch Fractal
def drawKoch(t, length, detail):
    if detail == 0:
        t.forward(length)
    else:
        drawKoch(t, length / 3.0, detail - 1)
        t.left(60)
        drawKoch(t, length / 3.0, detail - 1)
        t.right(120)
        drawKoch(t, length / 3.0, detail - 1)
        t.left(60)
        drawKoch(t, length / 3.0, detail - 1)

# Draws a dragon fractal.
# Inputs: turtle. Float. Nonnegative integer.
# Returns: None.
def drawDragon(t, length, detail):
	if detail == 0:
		t.forward(length)
	else:
		t.right(45)
		drawDragon(t, length/4 * math.sqrt(2), detail -1)
		t.left(90)
		drawDragon(t,length/2 * math.sqrt(2), detail-1)
		t.right(90)
		drawDragon(t,length/4 * math.sqrt(2), detail-1)
		t.left(45)


# Computes the sum of two lists of numbers (of equal length >= 0). 
# If the lists are empty, then returns the empty list.
# Input: List of numbers. List of numbers of the same length.
# Returns: List of numbers of the same length.
def listSum(a, b):
	if len(a) == 0:
		return []
	else:
		return [a[0]+b[0]] + listSum(a[1:],b[1:])


# Computes the sum of two arrays of numbers. 
# If the arrays are empty, then returns 0.
# Input: Array of numbers. Array of numbers of the same dimensions.
# Returns: Array of numbers of the same dimensions.
def arraySum(a, b):
	lst=[]
	if type(a) == int:
		return a+b
	else:
		for i in range(len(a)):
			lst += [arraySum(a[i],b[i])]
	return lst

#first = [[[[0, 1, 1], [1, -1, 4]], [[2, 1, 2], [3, 3, 1]], [[-5, -1, 3], [2, 2, 2]]]]
#second = [[[[5, 2, 2], [1, -1, 7]], [[2, 0, 0], [3, 9, 4]], [[4, 4, 4], [2, 2, 2]]]]
#arraySum(first, second) = [[[[5, 3, 3], [2, -2, 11]], [[4, 1, 2], [6, 12, 5]], [[-1, 3, 7], [4, 4, 4]]]]



