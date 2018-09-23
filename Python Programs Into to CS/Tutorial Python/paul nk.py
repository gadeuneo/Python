def paul(n,k):
	if n %2 ==0:
		return n // 2
	else:
		return 3*n + k
def mono(n,k):
	while n < 2:
		n = paul(n,k)
		print(n)
	print("end")

def mon(w):
	for i in range (1,10):
		mono(i,w)
print((mon(4)))