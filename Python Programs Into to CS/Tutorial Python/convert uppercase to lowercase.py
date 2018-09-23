upper = 'JDAVISTHEDOLPHINARRIVESATMIDNIGHTYOURFRIENDJBIEBER'
lower = ''
for character in upper:
    lower = lower + chr(ord(character) + 32)
print(lower)