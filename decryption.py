#!/bin/python

encrypted_target = open("target4.txt", "r")

var = encrypted_target.read()
characters = []
reset = 1

for i in var:
	i = ord(i)
	
	if i != 33:
		if reset == 1:
			i -= 7
			reset += 1
			i = chr(i)
			characters.append(i)
		elif reset == 2:
			i -= 4
			reset += 1
			i = chr(i)
			characters.append(i)
		elif reset == 3:
			i -= 6
			reset += 1
			i = chr(i)
			characters.append(i)
		elif reset == 4:
			i -= 7
			reset = 1
			i = chr(i)
			characters.append(i)

characters = '' .join(characters)

encrypted_target.close()

original_file = open("decrypted4.txt", "w")
original_file.write(characters)
original_file.close()

print("Decryption Done")
