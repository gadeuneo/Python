upper = 'JDAVISTHEDOLPHINARRIVESATMIDNIGHTYOURFRIENDJBIEBER'
lower = ''
for i in range(len(upper)):
	print(ord(upper[i]))
	lower = (ord(upper[i]) + 32)
	print(chr(lower))
print(lower)
