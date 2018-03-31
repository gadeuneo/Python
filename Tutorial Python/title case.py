#def titleCase(line):
#    return ' '.join([s[0].upper() + s[1:] for s in line.split(' ')])


#input = 'a fox mEt a dog'
#output = ''	
#def titleCase(input):
#	output = input.title()
#	return output
#print(titleCase(input))


def titleCase(a):
	answer = ''	
	for i in range(len(a)):
		if 'z' >= a[i] >= 'a'
			string1 = string1 + chr(ord(a[1]))

	for i in range(len(a)):
		if a[i-1] == "" or i == 0:
			answer += chr(ord(a[i]) - 32)
		else:
			answer += a[i]
		return answer
	
	
	
print(titleCase('example TeXt'))



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
