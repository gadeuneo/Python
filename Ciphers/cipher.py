# In this file, all plaintext strings are assumed to contain only spaces and upper-case Roman characters A, B, C, ..., Z. Each encryption system has an encryptor and a decryptor.

# Convert letters A, ..., Z to indices 0, ..., 25.
# Also handle a, ..., z, just because we can.
def indexFromLetter(char):
	if "A" <= char <= "Z":
		return ord(char) - ord("A")
	elif "a" <= char <= "z":
		return ord(char) - ord("a")
	else:
		return None

# Convert indices back to upper-case letters.
def letterFromIndex(index):
	if index < 0 or index > 25:
		return None
	else:
		return chr(index + ord("A"))



### RAIL FENCE ###

def railFenceEncryption(s):
	evens = ""
	odds = ""
	for i in range(len(s)):
		if i % 2 == 0:
			evens += s[i]
		else:
			odds += s[i]
	return evens + odds

def railFenceDecryption(s):
	evens = s[0:((len(s) + 1) // 2)]
	odds = s[((len(s) + 1) // 2):len(s)]
	answer = ""
	for i in range(len(odds)):
		answer += evens[i] + odds[i]
	if len(evens) > len(odds):
		answer += evens[-1]
	return answer



### ROT13 ###

def rot13Encryption(s):
	answer = ""
	for char in s:
		if char == " ":
			answer += char
		else:
			answer += letterFromIndex((indexFromLetter(char) + 13) % 26)
	return answer

rot13Decryption = rot13Encryption



### CAESAR ###

def caesarEncryption(s, n):
	answer = ""
	for char in s:
		if char == " ":
			answer += char
		else:
			answer += letterFromIndex((indexFromLetter(char) + n) % 26)
	return answer

def caesarDecryption(s, n):
	return caesarEncryption(s, -n)



### SUBSTITUTION ###

sub = "THEQUICKSLVRFOXJMPDAZYBWNG"

def substitutionEncryption(s, sub):
    answer = ""
    for char in s:
    	if char == " ":
    		answer += char
    	else:
        	answer += sub[indexFromLetter(char)]
    return answer

def substitutionInverse(sub):
	alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	inv = ""
	for i in range(0,26):
		for j in range(0,26):
			if sub[j] == chr(i + 65):
				inv += alp[j]
	return inv
# This function is correct as it is written. Do not alter it.
# It will work once you have a working version of substitutionInverse.
def substitutionDecryption(s, sub):
    return substitutionEncryption(s, substitutionInverse(sub))



### RE-IMPLEMENTING CAESAR IN TERMS OF SUBSTITUTION ###

def caesarEncryptionSub(s, n):
# !! This is where you re-write the Caesar encryption using substitutionEncryption.
	alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sub = ""
	for char in alp:
		if char == " ":
			sub += char
		else:
			sub += letterFromIndex((indexFromLetter(char) + n) % 26)
	#return sub
	answer = ""
	for char in s:
		if char == " ":
			answer += char
		else:
			answer += sub[indexFromLetter(char)]
	return answer




### REPEATED PAD ###
def repeatedPadIndex(plaintext, key):
	keyIndex = indexFromLetter(key)
	ptIndex = indexFromLetter(plaintext)
	newIndex = (ptIndex + keyIndex) % 26
	return letterFromIndex(newIndex)
	
def repeatedPadIndexD(plaintext, key):
	keyIndex = indexFromLetter(key)
	ptIndex = indexFromLetter(plaintext)
	newIndex = (keyIndex - ptIndex) % 26
	return letterFromIndex(newIndex)
	
plaintext = "SECRET DOLPHIN ATTACK AT NOON"
key = "GNIJIEB"
def repeatedPadEncryption(plaintext, key):
	answer = ""
	keyLen = len(key)
	for i in range(len(plaintext)):
		ch = plaintext[i]
		if ch == " ":
			answer += ch
		else:
			answer += repeatedPadIndex(key[i%keyLen], ch)
	return answer
encryptedtext = "YRKAMX JBTYPMO NBCIGL NB VSPT"
def repeatedPadDecryption(encryptedtext, key):
	# !! Replace the next line with code to compute and return the plaintext.
	answer = ""
	keyLen = len(key)
	for i in range(len(encryptedtext)):
		ch = encryptedtext[i]
		if ch == " ":
			answer += ch
		else:
			answer += repeatedPadIndexD(key[i%keyLen], ch)
	return answer



### BREAKING CAESAR ###
t = "KITZTMBWV KWTTMOM KA GMIP"
def caesarBreak(t):
	# !! Place code here to decrypt a Caesar cipher without knowing its key
	for i in range(0,26):
		answer = ""
		for char in t:
			if char == " ":
				answer += char
			else:
				answer += letterFromIndex((indexFromLetter(char) + i) % 26)
		print(i+1)
		print(answer)
	return None



### FREQUENCY ANALYSIS TO BREAK SUBSTITUTION ###

def stringFromFileName(fileName):
	with open(fileName) as file:
		return file.read()

def frequencies(string):
	#counts = []
	#for i in range(26):
	#	counts += [0]
	# Here's a Python trick to accomplish the preceding lines simply:
	# Multiplying a list by an integer concatenates that many copies of the list.
	counts = [0] * 26
	for char in string:
		index = indexFromLetter(char)
		if index != None:
			counts[index] += 1
	total = sum(counts)
	freqs = [0] * 26
	for i in range(len(counts)):
		freqs[i] = counts[i] / total
	return freqs

def main():
	s = "CARLETON COLLEGE CS YEAH"
	print("plaintext:")
	print(s)
	print("rail fence:")
	print(railFenceEncryption(s))
	print(railFenceDecryption(railFenceEncryption(s)))
	print("rot13:")
	print(rot13Encryption(s))
	print(rot13Decryption(rot13Encryption(s)))
	print("Caesar with key 8:")
	print(caesarEncryption(s, 8))
	print(caesarDecryption(caesarEncryption(s, 8), 8))
	print("Substitution:")
	print(substitutionEncryption(s, sub))
	print("Substitution(substitutionEncryption(s,sub),sub)")
	print(substitutionDecryption(substitutionEncryption(s,sub),sub))
	print("Repeated Pad Cipher")
	print(repeatedPadEncryption(plaintext,key))
	print("Repeated Pad Cipher repeatedPadDecryption(encryptedtext,key)")
	print(repeatedPadDecryption(encryptedtext, key))
	print("Caesar Encryption with Substitution (caesarEncryptionSub(s, n))")
	print(caesarEncryptionSub(s, 10))
	print("Caesar Break")
	print(caesarBreak(t))
	
	# !! Add code here to demonstrate the other ciphers, breaking Caesar, etc.

# If the user ran this file directly (rather than imported it), then do main.
if __name__ == "__main__":
	main()


