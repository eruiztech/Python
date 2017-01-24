#Edgar Ruiz
#CS 299
#Lab 1
#September 27th, 2016

#!/usr/bin/python

print("Lab 1")
print("Problem #4")
print("Calculate your BMI")
weight = int(input("Weight in kilograms: "))
height = int(input("Height in meters: "))
bmi = int(weight/(height*height))
print("Your BMI is: %d" % int(bmi))
print("Problem #5")
f = open('test.txt', 'w')
f.write('**************\n')
print("**************")
f.write('    ******	 \n')
print("    ******	 ")
f.write('Hello! How\'s everything?\n')
print("Hello! How's everything?")
f.write('There are 35 students in 1 session of CS 299 class.\n')
print("There are 35 students in 1 session of CS 299 class.")
f.write('Have a great quarter!\n')
print("Have a great quarter!")
f.close()
print("Problem #6 (Optional)")
print("test.txt file created with above lines from Problem #5")
print("Problem #7")
year = int(input("Type in a year: "))
print(year%4 == 0 and (not year%100 == 0 or year%400 == 0))
