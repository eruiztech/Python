#Edgar Ruiz
#CS 299
#Project 2-2
#Due: October 13th, 2016

#!/usr/bin/python

import turtle as turt
import time

def start(title):
    turt.hideturtle()
    turt.speed(0)
    turt.width(4)
    turt.title(title)
    turt.penup()
    turt.left(180)
    turt.forward(250)
    turt.right(90)
    turt.forward(30)
    turt.right(180)
    turt.pendown()

def printOne():
    turt.forward(30)
    turt.left(90)
    turt.penup()
    turt.forward(10)
    turt.left(90)
    turt.forward(30)
    turt.left(180)
    turt.pendown()

def printZero():
    turt.penup()
    turt.forward(15)
    turt.pendown()
    turt.forward(15)
    turt.left(90)
    turt.penup()
    turt.forward(10)
    turt.left(90)
    turt.forward(30)
    turt.left(180)
    turt.pendown()

def readInZip(strZip):
    noDash = ""
    for num in strZip:
        if num != "-":
            noDash += num
    return noDash

def checkSum(strZip):
    sum = 0
    for num in strZip:
        sum += int(num)
    check = 10 - (sum % 10)
    zipWCheck = strZip + str(check)
    return zipWCheck

def zipToBar(zipCode):
    clearDash = readInZip(zipCode)
    finalZipCode = checkSum(clearDash)
    turtleGuide = "1"  #1 is there to symbolize start
    for num in finalZipCode:
        if num == "0":
            turtleGuide += "11000"
        elif num == "1":
            turtleGuide += "00011"
        elif num == "2":
            turtleGuide += "00101"
        elif num == "3":
            turtleGuide += "00110"
        elif num == "4":
            turtleGuide += "01001"
        elif num == "5":
            turtleGuide += "01010"
        elif num == "6":
            turtleGuide += "01100"
        elif num == "7":
            turtleGuide += "10001"
        elif num == "8":
            turtleGuide += "10010"
        elif num == "9":
            turtleGuide += "10100"
    turtleGuide += "1" #1 is at the end to symbolize stop
    turtlePrint(turtleGuide, zipCode)

def turtlePrint(turtleGuide, zipCode):
    title = "Zip Code: " + zipCode
    start(title)
    for num in turtleGuide:
        if num == "0":
            printZero()
        else:
            printOne()
    finish()

def finish():
    time.sleep(3)
    turt.reset()

zipToBar(zipCode = "55555-1237")
zipToBar(zipCode = "91768-1234")
zipToBar(zipCode = "20500-0000")
turt.bye()
