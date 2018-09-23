


import turtle
import time

# Computes the factorial.
# Input: Nonnegative integer.
# Output: Positive integer.
def factorialIteratively(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

def factorialRecursively(n):
    if n == 0:
        return 1
    else:
        return n * factorialRecursively(n - 1)

# Computes the greatest common divisor.
# Assumes that not both of a and b are 0.
# Input: Nonnegative integer. Nonnegative integer.
# Output: Integer.
def euclideanIteratively(a, b):
    while b != 0:
        rem = a % b
        a = b
        b = rem
    return a

def euclideanRecursively(a, b):
    if b == 0:
        return a
    else:
        return euclideanRecursively(b, a % b)

# Returns the minimum of the list of numbers.
# Input: List of one or more numbers.
# Output: Number.
def minimumIteratively(l):
    m = l[0]
    for i in range(1, len(l)):
        if l[i] < m:
            m = l[i]
    return m

def minimumRecursively(l):
    if len(l) == 1:
        return l[0]
    else:
        m = minimumRecursively(l[1:])
        if l[0] < m:
            return l[0]
        else:
            return m

# Computes the nth Fibonacci number.
# Input: Nonnegative integer.
# Output: Integer.
def fibonacciRecursively(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursively(n - 1) + fibonacciRecursively(n - 2)

def fibonacciIteratively(n):
    old = 0
    new = 1
    for i in range(n):
        temp = old + new
        old = new
        new = temp
    return old

# Returns the power set of the given set.
# (The power set is the set of all subsets.)
# (A set is modeled as a list with no repeated elements.)
# Input: List.
# Output: List.
def powerSet(s):
    if len(s) == 0:
        return [[]]
    else:
        subsets = powerSet(s[1:])
        result = []
        for i in range(len(subsets)):
            result.append(subsets[i])
        for i in range(len(subsets)):
            result.append([s[0]] + subsets[i])
    return result

# What happens when you call a("2")? a(2)? Why?
def a(x):
    return b(x)

def b(x):
    return c(x)

def c(x):
    return x + "1"

# What happens when you call factorialBadly(4)? Why?
def factorialBadly(n):
    if n == 0:
        print(1)
    else:
        return n * badFact(n - 1)

# Draws a tree fractal of the specified trunk length.
# Try drawTree(turtle.getturtle(), 100).
# Input: turtle. Float.
# Output: None.
def drawTree(t, trunkLength):
    if trunkLength >= 5:
        t.forward(trunkLength)
        t.right(30)
        drawTree(t, trunkLength - 15)
        t.left(60)
        drawTree(t, trunkLength - 15)
        t.right(30)
        t.backward(trunkLength)

# Draws the Sierpinski fractal.
# Try drawSierpinski(turtle.getturtle(), (-200, -173), (200, -173), (0, 173), 6).
# Input: turtle. Pair of numbers. Pair of numbers. Pair of numbers. Non-negative integer.
# Output: None.
def drawSierpinski(t, a, b, c, detail):
    if detail == 0:
        # Draw triangle.
        t.up()
        t.goto(a)
        t.down()
        t.goto(b)
        t.goto(c)
        t.goto(a)
    else:
        # Compute the midpoints of the three sides.
        ab = [(a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0]
        bc = [(b[0] + c[0]) / 2.0, (b[1] + c[1]) / 2.0]
        ca = [(c[0] + a[0]) / 2.0, (c[1] + a[1]) / 2.0]
        # Draw three subfractals.
        drawSierpinski(t, a, ab, ca, detail - 1)
        drawSierpinski(t, b, bc, ab, detail - 1)
        drawSierpinski(t, c, ca, bc, detail - 1)

# Draws a logarithmic spiral filled with triangles, like a 
# nautilus shell. Try 
# drawLogarithmicSpiral(turtle.getturtle(), 200.0, 190.0, 20, 18).
# Input: turtle. Initial radius float. Second 
# radius float. Float angle between those two radii, in 
# degrees. Positive integer number of chambers.
def drawLogarithmicSpiral(t, r0, r1, angle, count):
    if count >= 1:
    	# Draw a triangle with sides r0 and r1, and the given angle between them.
        a = t.position()
        t.forward(r0)
        b = t.position()
        t.goto(a)
        t.left(angle)
        t.forward(r1)
        t.goto(b)
        t.goto(a)
        # Repeat.
        drawLogarithmicSpiral(t, r1, r1 * r1 / r0, angle, count - 1)

# Draws a Koch snowflake of the given side length and level of detail.
# Try drawKoch(turtle.getturtle(), 300, 4).
# Input: turtle. Float. Nonnegative integer.
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

def main():
    #startTime = time.clock()
    #for i in range(32):
    #    temp = fibonacciIteratively(i)
    #endTime = time.clock()
    #print()
    #print("Iterative Fibonacci took", endTime - startTime, "seconds")
    startTime = time.clock()
    #for i in range(32):
    #    temp = fibonacciRecursively(i)
    #endTime = time.clock()
    #print()
    #print("Recursive Fibonacci took", endTime - startTime, "seconds")
    #drawTree(turtle.getturtle(), 100)
    #drawSierpinski(turtle.getturtle(), (-200, -173), (200, -173), (0, 173), 6)
    #drawLogarithmicSpiral(turtle.getturtle(), 200.0, 190.0, 20, 18)
    drawKoch(turtle.getturtle(), 300, 4)

if __name__ == "__main__":
    main()

