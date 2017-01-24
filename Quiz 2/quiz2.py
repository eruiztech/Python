#Edgar Ruiz
#CS 299
#Quiz 2
#October 13th, 2016

#!/usr/bin/python

def myAve(*args):
    sum = 0
    count = 0
    for arg in args:
        if type(arg) == type(1):
            sum += arg
            count += 1
    if count > 0:
        sum = float(sum/count)
    else:
        sum = 0.0
    return sum

print("Quiz 2 Part 2 Problem B1")
print(myAve(3, 2.5, 2, 3.4, 4))
print(myAve())
print(myAve(5, '5', 6, 'abc', 5.0))

def cript(num):
    strNum = str(num)
    count = 0
    for digit in strNum:
        count += 1
    if count == 4:
        counter = 0
        newStrDigit = ""
        strDigitOne = ""
        strDigitTwo = ""
        strDigitThree = ""
        for digit in strNum:
            intDigit = int(digit)
            modDigit = (intDigit + 7) % 10
            counter += 1
            if counter == 1:
                strDigitOne += str(modDigit)
            elif counter == 2:
                strDigitTwo += str(modDigit)
            elif counter == 3:
                strDigitThree += str(modDigit)
            else:
                newStrDigit = strDigitThree + str(modDigit) + strDigitOne + strDigitTwo
                return newStrDigit
    else:
        print("Number must be 4 digits long")

print("Quiz 2 Part 2 Problem B2 Alternate")
print("Here are two test cases")
print("Number inputted: 3214\nEncrypted number: ", cript(3214))
print("Number inputted: 1009\nEncrypted number: ", cript(1009))
print("You can try it now")
num = input("Please enter 4 digit integer to be encrypted: ")
print("Your encrypted number is: ", cript(num))
