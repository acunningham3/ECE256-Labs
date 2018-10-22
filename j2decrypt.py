#!/bin/python

encrypted_target = open("target5j.txt", "r")

var = encrypted_target.read()

characters = []


count = 0

for i in var:
	i = ord(i)
	if (i - count) == 90:
		i = 10 + count
	i -= count
	i = chr(i)
	characters.append(i)
	count += 1
	if count >= 7:
		count = 0

characters = '' .join(characters)

encrypted_target.close()

original_file = open("decrypted.txt", "w")

original_file.write(characters)

original_file.close()

print("Decryption Done")

