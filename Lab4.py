#Edgar Ruiz
#CS 299
#Lab 4
#October 18th, 2016

#!/usr/bin/python

import math

def reverse(MyList):
    revList = []
    count = -1
    for item in MyList:
        revList.append(MyList[count])
        count -= 1
    return revList

def place(element, MyList):
    index = 0
    for item in MyList:
        if element == item:
            return index
        index += 1
    return -1

def med(MyList):
    MyList.sort()
    print("List sorted for reference: ", MyList)
    if len(MyList) % 2 == 0:
        leftMed = int(len(MyList) / 2)
        rightMed = int(leftMed - 1)
        med = float((MyList[leftMed] + MyList[rightMed]) / 2)
        return med
    else:
        medianIndex = int(len(MyList) / 2)
        med = MyList[medianIndex]
        return med

print("Lab 4 Problem 1")
MyList = ["Hello", 7, 7, 9, 'a', 'cat', False]
print("MyList current state: ", MyList)
MyList.append(math.pi)
MyList.append(7)
print("Added Pi and 7 to list")
print("MyList current state: ", MyList)
MyList.insert(2, 'dog')
print("Inserted dog at position 3")
print("MyList current state: ", MyList)
print("Index of cat is: ", MyList.index('cat'))
print("MyList current state: ", MyList)
print("Count of number of 7's in the list is: ", MyList.count(7))
print("MyList current state: ", MyList)
del MyList[1]
print("Removed first 7 from the list")
print("MyList current state: ", MyList)
MyList.pop(1)
print("Removed dog using pop and index")
print("MyList current state: ", MyList)
print("Problem 2")
print("MyList reversed: ", reverse(MyList))
print("Index is returned if found or -1 is returned if not found")
print("Find index of 9: ", place(9, MyList))
print("Find index of bye: ", place("bye", MyList))
aList = [24,5,8,2,9,15,10]
print("Find median of [24,5,8,2,9,15,10]: ", med(aList))
bList = [24,5,8,2,9,15,10,54]
print("Find median of [24,5,8,2,9,15,10,54]: ", med(bList))




