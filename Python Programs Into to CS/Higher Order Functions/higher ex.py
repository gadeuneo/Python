### MAP: APPLY A FUNCTION TO EACH ELEMENT IN A LIST ###

# Very frequently we want to apply a function to each item in a list.
# Here's an example using a for loop.
l = range(10)
m = []
for item in l:
	m += [item ** 3]
m

# This task is so common that there is a function, called map, just for it.
l = range(10)
def cube(x):
	return x ** 3
list(map(cube, l))



### FILTER: SELECT A SUBLIST ACCORDING TO SOME CRITERION ###

# Another common task is to select the list items that satisfy some test.
# Here's an example using a for loop.
l = range(10)
m = []
for item in l:
	if item % 2 == 0:
		m += [item]
m

# Here's how to do it with the filter function.
l = range(10)
def isEven(n):
	return n % 2 == 0
list(filter(isEven, l))



### REDUCE: COMBINE ELEMENTS IN A LIST USING SOME OPERATION ###

# A third common task is to combine list elements using some operation.
# Here's an example using a for loop.
l = range(10)
total = 0
for item in l:
	total += item
total

# Here's how to do it with the reduce function.
l = range(10)
def summation(x, y):
	return x + y
import functools
functools.reduce(summation, l)



### HOW THESE CAN SAVE YOU WORK ###

# map, filter, and reduce don't save you a lot of coding, 
# if you have to write a helper function each time you use them.
# In the reduce example, do we really have to write our own addition function?
# Python obviously has addition, but neither of these lines works.
functools.reduce(+, range(10))
functools.reduce('+', range(10))

# The function you want is add, in the operator module.
import operator
functools.reduce(operator.add, range(10))

# In general, Python might not have a built-in function for your task.
# You can use the lambda keyword to make a function right when you need it.
# Here are our three examples, in one line of code each.
functools.reduce(lambda x, y: x + y, range(10))

list(filter(lambda n: n % 2 == 0, range(10)))

list(map(lambda x: x ** 3, range(10)))



### GEOMETRIC MEAN EXAMPLE ###

# The geometric mean of a list of n numbers is the nth root of their product.
# This function computes it.
def geomMean(l):
	return (functools.reduce(lambda x, y: x * y, l)) ** (1 / len(l))

# Here are some examples. Interestingly, the second one is imprecise.
geomMean([1, 9])
geomMean([1, 10, 100])



### PAYROLL EXAMPLE ###

# Imagine that you manage payroll at a company.
# You've got a list of employees, each with birth date and salary.
employees = [["Tova Ughdahl", 1989, 44000], ["He Yongsheng", 1996, 52000], ["Babatope Ogunmola", 1976, 51000], ["Jack Johnson", 1994, 42000], ["John Jackson", 1994, 41000], ["Jorge Amarillo", 1972, 61000], ["Jessica Jones", 1977, 9000]]

# Here's how you might compute the total payroll using a for loop.
total = 0
for emp in employees:
	total += emp[2]
total

# Or you could compute the total payroll in one line as follows.
functools.reduce(lambda x, y: x + y, map(lambda x: x[2], employees))



### TIC TAC TOE EXAMPLE ###

# We have studied several ways to implement hasWon for Tic Tac Toe.
# In one of the implementations, we listed ways to win,
# and then looped over those ways, testing whether any of them worked.
# Here's an implementation using map and reduce.
def hasWon(b, p):
	ways = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]], [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
	def hasWonByWay(way):
		return b[way[0][0]][way[0][1]] == b[way[1][0]][way[1][1]] == b[way[2][0]][way[2][1]] == p
	hasWonWays = map(hasWonByWay, ways)
	return functools.reduce(operator.or_, hasWonWays)

