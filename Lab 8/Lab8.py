#Edgar Ruiz
#CS 299
#Lab 8
#November 15th, 2016

#!/usr/bin/python

def revString(line, newLine = ""):
    if len(newLine) == len(line):
        return newLine
    else:
        newLine += line[len(line) - len(newLine) - 1]
        return revString(line, newLine)

def pattern(num):
    if num == 0:
        print(num, end = ' ')
    else:
        pattern(num-1)
        print(num, end = ' ')
        pattern(num-1)

def gSort(function, list1):
    if function == "le":
        print(leSort(list1))
    elif function == "ge":
        print(geSort(list1))
    elif function == "hCount":
        print(hCSort(list1))

def leSort(list1):
    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            if list1[j] < list1[j+1]:
                list1[j+1], list1[j] = list1[j], list1[j+1]
    return list1

def geSort(list1):
    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j+1]:
                list1[j+1], list1[j] = list1[j], list1[j+1]
    return list1

def hCSort(list1):
    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j+1]:
                list1[j+1], list1[j] = list1[j], list1[j+1]
    return list1

def mapFilter(list1):
    list2 = list(map((lambda x: x*2), list1))
    list3 = [x**2 for x in list1 if x%2 == 1]
    list4 = [x for x in list1 if not[y for y in range(2, x) if not x % y]]
    return list2, list3, list4

print("Problem 1")
print(revString("abc"))
print(revString("hello, world!"))
print("Problem 2")
pattern(0)
print()
pattern(1)
print()
pattern(2)
print()
pattern(3)
print()
pattern(4)
print()
print("Problem 3")
gSort("le", [5, 2, 12, 4, 9, 13, 22, 1, 6, 17])
gSort("ge", ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob", "Joy"])
gSort("hCount", [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1), ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)])
list5 = mapFilter([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print("Problem 4")
print(list5[0])
print(list5[1])
print(list5[2])

"""
Output

Problem 1
cba
!dlrow ,olleh
Problem 2
0 
0 1 0 
0 1 0 2 0 1 0 
0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 
0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 4 0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 
Problem 3
[22, 17, 13, 12, 9, 6, 5, 4, 2, 1]
['Alp', 'Alpine', 'Beta', 'Bob', 'Jolly', 'Joy', 'Kate', 'Kate', 'Sam', 'Samuel']
[('Alp', 1), ('Alp', 2), ('Alpine', 2), ('Beta', 3), ('Bob', 2), ('Jolly', 1), ('Kate', 3), ('Kate', 5), ('Sam', 2), ('Sam', 3), ('Sam', 4)]
Problem 4
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
[1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
[1, 2, 3, 5, 7, 11, 13, 17, 19]
"""
