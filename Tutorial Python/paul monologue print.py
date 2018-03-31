mono = 1
for i in range(101):
	while i > 1:
		if(i % 2) <= 0:
			i = i//2
			mono = mono + 1
		else:
			i = i * 3 + 1
			mono = mono + 1
	print(mono)