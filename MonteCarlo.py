#Edgar Ruiz
#CS 299
#Lab 3 Problem 1
#Due: October 6th, 2016

#!/usr/bin/python

import random
import time

print("Lab 3\nMonte Carlo Problem\n")

def MonteCarlo(n):
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
	print("Value of n: ", n)
	print("Pi value: ", pi) 
	print("Execution time: ", totalTime, " seconds\n")

MonteCarlo(10000)
MonteCarlo(100000)
MonteCarlo(1000000)