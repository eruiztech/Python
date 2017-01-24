#Edgar Ruiz
#CS 299
#Lab 2
#September 29th, 2016

#!/usr/bin/python

print("Lab 2")
print("Calculate your BMI")
unitChoice = input("Would you like to use (1) kilograms/meters or (2) pounds/inches as units?\nPlease enter 1 or 2\n")
if unitChoice == 1:
	weight = float(input("Weight in kilograms: "))
	height = float(input("Height in meters: "))
	bmi = float(weight/(height*height))
elif unitChoice == 2:
	weight = float(input("Weight in pounds: "))
	height = float(input("Height in inches: "))
	bmi = float((weight/(height*height)) * 703)
else:
	print("invalid choice")
	exit()
print("Your BMI is: %d" % int(bmi))
if int(bmi) <= 24:
	print("you have a normal BMI")
elif int(bmi) >= 25 and int(bmi) <= 29:
	print("you are considered overweight")
elif int(bmi) >= 30 and int(bmi) <= 39:
	print("you are considered obese")
else:
	print("you are extremely obese")



