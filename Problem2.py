#!/usr/bin/python

x = input("Enter number to test if it is prime: ")

count = x // 2
while count > 0:
	if x % count == 0 and count != 1:
		print("This is not a prime number")
		break
	count -= 1
else:
	print("This is a prime number")