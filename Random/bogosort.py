import random
from time import *


def createArray(n):
	x = []
	for i in range(0,n):
		x.append(random.randint(0, (n)))
	return x


def sorted(array):
	i = 0
	j = len(array)
	while i + 1 < j:
		if array[i] > array[i+1]:
			return False
		i += 1
	return True

def bogoSort(array):
	while not sorted(array):
		random.shuffle(array)
	return array
		
if __name__ == '__main__':
	try:
		raw_input
	except NameError:
		raw_input = input
	
	user_input = int(raw_input('Enter number of integers to bogoSort: '))
	start = time()
	b = createArray(user_input)
	
	if (user_input < 20):
		print("Generated List: ",b)
		print("Sorted List: ",bogoSort(b))
	else:
		bogoSort(b)
	print("%.2f seconds" % (time() - start))
	