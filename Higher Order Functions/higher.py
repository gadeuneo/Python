#JAMES GARDNER














#We have learned three higher-order functions: map, filter, and reduce. Another popular higher-order function is thread. This function takes in a function f and two lists of equal length. The function f takes two inputs (not just one, as in map), and returns some output. The function thread returns a list, of equal length to its two input lists. Each item in the output list is the result of applying f to the corresponding items in the two input lists.

#Question A: Write thread. Do not use a loop; instead use map. My solution is two lines of code. The first line of your code should be
#HINT: INSTEAD OF MAPPING OVER LISTA OR LISTB MAP OVER A RANGE

def thread(f, listA, listB):
	return list(map(lambda i:f(listA[i], listB[i]), range(len(listA))))

#Question B: Rewrite dot to accomplish its task using thread and reduce. My solution is two lines of code.
v = [1,2,3]
w = [3,2,2]
def dot(v,w):
	return functools.reduce(lambda x,y:x+y,(thread(lambda v,w: v*w, v, w)))


#The following two questions concern a function called mystery. This function takes as input an integer n. As output it returns None. While it is running, it prints various numbers to the screen. Here is the algorithm in English.

#1) Begin with the list of numbers range(2, n).
#2) Repeat until the list is empty:
#3) Print the first (0th) number in the list.
#4) Remove all numbers from the list that are divisible by that first number.
#5) Return None.

#Question C: Write the function mystery in Python. You must use filter for the number-removal step. My solution is six lines of code.

def mystery(n):
	l = range(2,n)
	while len(l) >= 1:
		print(l[0])
		l =list(filter(lambda i: i % l[0], l))
	return None

#Question D: Try your function for various values of n, such as 100. What is mathematically special about the numbers that mystery prints? Answer this question in English, placing it in a comment in higher.py.


#Answer to D: All of the numbers printed by mystery are PRIME NUMBERS!!!






#Thus far, all of our higher-order functions have taken a function as one of their inputs. But we also call a function higher-order when it returns a function as its output.

#Question E: Write a function called isDivisibleBy. As input it takes a positive integer n. As output it returns a function f with the following properties. This f takes as input a single integer m. As output, f returns a Boolean indicating whether m is divisible by n. My solution is two lines of code. The following transcript is an example of how one might use this isDivisibleBy function.

#>>> isDivisibleBy7 = isDivisibleBy(7)
#>>> isDivisibleBy7(14)
#True
#>>> isDivisibleBy7(15)
#False
#>>> isDivisibleBy(9)(18)
#True
#>>> list(map(isDivisibleBy(3), range(10)))
#[True, False, False, True, False, False, True, False, False, True]



def isDivisibleBy(n):
	return lambda m: m %n == 0





















