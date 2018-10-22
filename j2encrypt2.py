#!/bin/python

encrypted_target = open("Group5Lab2.txt", "r")

var = encrypted_target.read()

characters = []


count = 0

for i in var:
	i = ord(i)
	if i == 10:
		i = 90
	i += count
	i = chr(i)
	characters.append(i)
	count += 1
	if count >= 7:
		count = 0

characters = '' .join(characters)

encrypted_target.close()

original_file = open("target5j.txt", "w")

original_file.write(characters)

original_file.close()

print("Encryption Completed")

