#Edgar Ruiz
#CS 299
#Exam 2 Part 2
#November 22, 2016

#!/usr/bin/python

import string
import queue

try:
    f = open("names.txt", "r")
    names = []
    for line in f:
        newName = str(line)
        names.append(newName[:-1])   #deletes '\n'
    f.close()
    print("Users from file: ", names)
except:
    print("File not found")
try:
    fp = open("password.txt", "r")
    passwords = []
    for line in fp:
        newPass = str(line)
        passwords.append(newPass[:-1])  #delets '\n'
    fp.close()
    print("Passwords from file: ", passwords)
except:
    print("File not found")
login = dict(zip(names, passwords))
for key in login.keys():
    newPass = ""
    for x in login[key]:
        if x in string.digits or x in string.ascii_letters:
            newPass += x
    login[key] = newPass
line = queue.Queue()
line.put("Jim")
line.put("Terry")
line.put("Carter")
user = str(input("Tim, please enter user name: "))
pw = str(input("Password: "))
if user in login:
    if login[user] == pw:
        line.put("Tim")
        print("Access granted, you have been added to the queue")
else:
    print("Invalid Login")
line.get("Jim")
