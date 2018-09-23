def isOdd(n):
	if n % 2 != 0:
		return True
	else:
		return False
print(isOdd(5))



x=[1,2,2]
y=[3,2,5]
def dot(x,y):
	total = 0
	for i in range(len(x)):
		total = total + x[i] * y[i]
	return total
print(dot(x,y))



def titleCase(a):
	grammar = ''
	for i in range(len(a)):
		if a[i-1] == ' ' and "a" <= a[i] <= "z":
			grammar = grammar + chr(ord(a[i])-32)
		elif "A" <= a[i] <= "Z" and a[i-1] != ' ':
			if i==0:
				grammar = grammar + chr(ord(a[i]))
			else:
				grammar = grammar + chr(ord(a[i]) + 32)
		else:
			grammar = grammar + a[i]
	return(grammar)
print(titleCase("me EdId")



def isPrime(n):
    if n < 2:
        return False
    if n == 2: 
        return True
    if not n & 1: 
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
print(isPrime(3))

