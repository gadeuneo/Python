def paul(n, k):
	while n > 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = 3 * n + k
	print(paul(15, 1))


