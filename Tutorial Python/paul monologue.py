number = 16
mono = 1
while number > 1:
	if(number % 2) <= 0:
		number = number//2
		mono = mono + 1
	else:
		number = number * 3 + 1
		mono = mono + 1
print(mono)