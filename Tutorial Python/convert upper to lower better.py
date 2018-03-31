string = 'JDAVISTHEDOLPHINARRIVESATMIDNIGHTYOURFRIENDJBIEBER'
result = ''
for character in string:
    if (character < 'a'): 
        result = result + chr(ord(character) + 32)
    else:
        result = result + character
print(result)