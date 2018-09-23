


# An expression is a number (float or int), a string representing a variable or constant, or a list in which the first entry is a string representing a function and the other entries are expressions representing arguments to that function. Here are some examples:
# 13
# -4.21
# pi
# e
# 'x'
# ['sin', 1.57]
# ['+', 'y', 4, 'lobster']
# ['*', 3, ['-', 'x', 10], ['-', 'x']]
# +, * can take any number >= 0 of arguments.
# - can take 1 or 2 arguments, meaning negation or subtraction.
# /, ^ take 2 arguments.
# sqrt, sin, cos, exp, log take 1 argument.



import math
import operator
import functools

funcs = {'sqrt':(lambda vals: math.sqrt(vals[0])), 'sin':(lambda vals: math.sin(vals[0])), 'cos':(lambda vals: math.cos(vals[0])), 'exp':(lambda vals: math.exp(vals[0])), 'log':(lambda vals: math.log(vals[0]))}
# '+':math.fsum, '-':(lambda vals: functools.reduce(operator.sub, vals, 0)), '*':(lambda vals: functools.reduce(operator.mul, vals)), '/':operator.div, '^':math.pow

def beauty(expr):
	"""Given an expression, returns a string for the expression in a standard mathematical infix format."""
	if (type(expr) == int or type(expr) == float):
		return str(expr)
	elif (type(expr) == str):
		return expr
	elif (expr[0] == '+' or expr[0] == '*' or expr[0] == '/' or expr[0] == '^'):
		s = "(" + beauty(expr[1])
		for term in expr[2:]:
			s += " " + expr[0] + " " + beauty(term)
		s += ")"
		return s
	elif (expr[0] == '-'):
		if (len(expr) == 2):
			return "-" + beauty(expr[1])
		else:
			return "(" + beauty(expr[1]) + " - " + beauty(expr[2]) + ")"
	else:
		s = beauty(expr[1])
		if (s[0] == '('):
			return expr[0] + s
		else:
			return expr[0] + "(" + s + ")"

def value(expr, var, val):
	"""Given an expression, a string, and a float, regards the string as a variable name, and plugs the float into the expression for that variable. Frequently you want to follow this function with simplification."""
	if (type(expr) == int or type(expr) == float):
		return float(expr)
	elif (type(expr) == str):
		if (expr == var):
			return float(val)
		else:
			return expr
	else:
		vals = [value(term, var, val) for term in expr[1:]]
		return [expr[0]] + vals

def simplificationOfSpecial(terms, expr0):
	"""Helper function for simplification."""
	if (type(terms[0]) == float):
		return funcs[expr0](terms)
	else:
		return [expr0, terms[0]]

def simplificationOfSum(terms):
	"""Helper function for simplification."""
	numbers = list(filter(lambda term: (type(term) == float), terms))
	others = list(filter(lambda term: (type(term) != float), terms))
	number = math.fsum(numbers)
	if (len(others) == 0):
		return number
	elif (number == 0.0):
		if (len(others) == 1):
			return others[0]
		else:
			return ['+'] + others
	else:
		return ['+', number] + others

def simplificationOfProduct(terms):
	"""Helper function for simplification."""
	numbers = list(filter(lambda term: (type(term) == float), terms))
	others = list(filter(lambda term: (type(term) != float), terms))
	number = functools.reduce(operator.mul, numbers, 1.0)
	if (len(others) == 0):
		return number
	elif (number == 0.0):
		return 0.0
	elif (number == 1.0):
		if (len(others) == 1):
			return others[0]
		else:
			return ['*'] + others
	else:
		return ['*', number] + others

def simplificationOfDifference(terms):
	"""Helper function for simplification."""
	if (len(terms) == 1):
		if (type(terms[0]) == float):
			return -terms[0]
		else:
			return ['-', terms[0]]
	else:
		if (type(terms[0]) == float and type(terms[1]) == float):
			return terms[0] - terms[1]
		elif (terms[0] == 0.0):
			return ['-', terms[1]]
		elif (terms[1] == 0.0):
			return terms[0]
		else:
			return ['-', terms[0], terms[1]]

def simplificationOfQuotient(terms):
	"""Helper function for simplification."""
	if (terms[0] == 0.0):
		return 0.0
	elif (type(terms[1]) == float):
		if (type(terms[0]) == float):
			return terms[0] / terms[1]
		else:
			return ['*', 1.0 / terms[1], terms[0]]
	else:
		return ['/', terms[0], terms[1]]

def simplificationOfPower(terms):
	"""Helper function for simplification."""
	if (terms[0] == 0.0 or terms[0] == 1.0):
		return terms[0]
	elif (terms[1] == 0.0):
		return 1.0
	elif (terms[1] == 1.0):
		return terms[0]
	elif (type(terms[0]) == float and type(terms[1]) == float):
		return math.pow(terms[0], terms[1])
	else:
		return ['^', terms[0], terms[1]]

def simplification(expr):
	"""Simplifies the expression, collapsing numerical arguments and using various rules of algebra."""
	if (type(expr) == int or type(expr) == float):
		return float(expr)
	elif (type(expr) == str):
		if (expr == 'pi'):
			return math.pi
		elif (expr == 'e'):
			return math.e
		else:
			return expr
	else:
		terms = [simplification(term) for term in expr[1:]]
		if (expr[0] == 'sqrt' or expr[0] == 'sin' or expr[0] == 'cos' or expr[0] == 'exp' or expr[0] == 'log'):
			return simplificationOfSpecial(terms, expr[0])
		elif (expr[0] == '+'):
			return simplificationOfSum(terms)
		elif (expr[0] == '-'):
			return simplificationOfDifference(terms)
		elif (expr[0] == '*'):
			return simplificationOfProduct(terms)
		elif (expr[0] == '/'):
			return simplificationOfQuotient(terms)
		else:
			return simplificationOfPower(terms)

def main():
	expr = ['sin', ['+', ['*', 'x', 4], 'y', 'z']]
	print(expr)
	print(beauty(expr))
	print(value(expr, 'x', 7))
	print(simplification(value(expr, 'x', 7)))
	print(beauty(simplification(value(expr, 'x', 7))))

if __name__ == "__main__":
	main()

