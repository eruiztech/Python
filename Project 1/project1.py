#Edgar Ruiz
#CS 299
#Project 1
#Due: October 4th, 2016

#!/usr/bin/python

import random
import time

print("Project 1")
print("Problem 1")
print("Welcome to Rock, Paper, Scissors!")
choices = ["Rock", "Paper", "Scissors"]
userChoice = int(input("Enter (0) for Rock, (1) for Paper, or (2) for Scissors: "))
compChoice = int(random.random() * 100) % 3
print("You chose: %s" % choices[userChoice])
print("Computer chose: %s" % choices[compChoice])
if userChoice == compChoice:
	print("Draw")
elif (userChoice == 0 and compChoice == 1) or (userChoice == 1 and compChoice == 2) or (userChoice == 2 and compChoice == 0):
	print("Computer wins!")
else:
	print("You win!")
print("***************************")
print("Problem 2")
num = int(input("Please enter a number to check if it is a perfect number: "))
factorL = []
count = num//2
sum = 0
while count > 0:
	if num % count == 0:
		factorL.append(count)
		sum = sum + count
	count -= 1
if sum == num:
	print num, "is a perfect number,", num, "=", factorL[-1],
	for num in reversed(factorL[:-1]):
		print "+ %d" % num,
else:
	print num, "is not a perfect number.",
print("\n***************************")
print("Problem 3")
n = int(input("Enter number of random points: "))
startTime = time.time()
pointCount = 0
for num in range(n):
	x = random.uniform(0,1)
	y = random.uniform(0,1)
	equation = float((x * x) + (y * y))
	if equation <= 1:
		pointCount = pointCount + 1
p = float(float(pointCount) / float(n))
pi = float(p * 4)
endTime = time.time()
totalTime = endTime - startTime
print "Value of n: ", n 
print "Pi value: ", pi 
print "Execution time: ", totalTime, " seconds"
	
