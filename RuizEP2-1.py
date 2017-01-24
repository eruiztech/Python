#Edgar Ruiz
#CS 299
#Project 2-1
#Due: October 13th, 2016

#!/usr/bin/python

import random
import string

alphabet = string.ascii_lowercase

def substitutionEncrypt(plainTxt, key):
	cipherTxt = ""
	for letter in plainTxt:
		for count in range(26):
			if alphabet[count] == letter:
				cipherTxt += key[count]
				break
	return cipherTxt	

def substitutionDecrypt(cipherTxt, key):
	decipherTxt = ""
	for letter in cipherTxt:
		for count in range(26):
			if key[count] == letter:
				decipherTxt += alphabet[count]
				break
	return decipherTxt

def keyGen():
	key = "".join(random.sample(alphabet, len(alphabet)))
	return key

def testDrive(*strings, key = "bpzhgocvjdqswkimlutneryaxf", tag = "E"):
	print("\nThe key being used is: ", key)
	for str in strings:
		if tag == "D":
			print("Encrypted string: ", str)
			decipherTxt = substitutionDecrypt(str, key)
			print("Decrypted string: ", decipherTxt)
		elif tag == "E":
			print("Original string: ", str)
			cipherTxt = substitutionEncrypt(str, key)
			print("Encrypted string: ", cipherTxt)
		else:
			print("Error: Wrong tag used")


testDrive("flow", "substitutioncipher", tag = "E")
testDrive("flow", "substitutioncipher", key = keyGen(), tag = "E")
testDrive("osiy", "obzy", "doedlugvusu", tag = "D")
testDrive("osiy", "obzy", "doedlugvusu", key = keyGen(), tag = "D")

"""
Output


The key being used is:  bpzhgocvjdqswkimlutneryaxf
Original string:  flow
Encrypted string:  osiy
Original string:  substitutioncipher
Encrypted string:  teptnjnenjikzjmvgu

The key being used is:  gkbfdsqthpvmiruxayezwlnjco
Original string:  flow
Encrypted string:  smun
Original string:  substitutioncipher
Encrypted string:  ewkezhzwzhurbhxtdy

The key being used is:  bpzhgocvjdqswkimlutneryaxf
Encrypted string:  osiy
Decrypted string:  flow
Encrypted string:  obzy
Decrypted string:  facw
Encrypted string:  doedlugvusu
Decrypted string:  jfujqrehrlr

The key being used is:  mdbgfqevwjhpuiatxnlkozcrsy
Encrypted string:  osiy
Decrypted string:  uynz
Encrypted string:  obzy
Decrypted string:  ucvz
Encrypted string:  doedlugvusu
Decrypted string:  bugbsmdhmym
"""


