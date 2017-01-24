#Edgar Ruiz
#CS 299
#Project 3
#November 1st, 2016

#!/usr/bin/python

#This is for a 1 month period worldwide. Graph auto updates based on feed from USGS.

import turtle
import urllib.request

histo = turtle.Turtle()

def drawBar(barWidth, barHeight):
    histo.forward(barHeight)
    histo.right(90)
    histo.forward(barWidth)
    histo.right(90)
    histo.forward(barHeight)
    histo.right(180)

def skipBar(barWidth):
    histo.penup()
    histo.right(90)
    histo.forward(barWidth)
    histo.left(90)
    histo.pendown()

def drawDashes():
    for num in range(4):
        histo.forward(100)
        histo.left(90)
        histo.forward(10)
        histo.write((num+1)*50, align = "left")
        histo.right(180)
        histo.forward(10)
        histo.left(90)

def writeNum(item):
    histo.penup()
    histo.right(180)
    histo.forward(10)
    histo.write(item, align="left")
    histo.right(180)
    histo.forward(10)
    histo.pendown()

def printHisto(magTup, xMin, xMax):
    turtle.screensize(640, 480)
    histo.speed(0)
    histo.hideturtle()
    histo.penup()
    histo.right(90)
    histo.forward(140)
    histo.left(90)
    histo.forward(300)
    histo.right(180)
    histo.pendown()
    histo.forward(600)
    histo.right(90)
    drawDashes()
    histo.penup()
    histo.right(180)
    histo.forward(400)
    histo.right(180)
    histo.pendown()
    barWidth = int(600/((xMax - xMin)*10))
    counterList = []
    for num in range(int(((xMax - xMin)+0.1)*10)):
        counterList.append(xMin + float(num/10))
    num = 0
    counter = 0
    for item in counterList:
        if magTup[num][0] == item:
            barHeight = magTup[num][1] * 2
            if counter % 2 == 0:
                writeNum(item)
            drawBar(barWidth, barHeight)
            num += 1
            counter += 1
        else:
            if counter % 2 == 0:
                writeNum(item)
            skipBar(barWidth)
            counter += 1

def earthquakeCount(pageText):
    magnitudes = []
    for num in range(len(pageText)-1):
        info = str(pageText[num+1]).split(",")
        magnitudes.append(round(float(info[4]), 1))
    magnitudes.sort()
    count = 0
    magSet = []
    magCount = []
    for num in range(len(magnitudes)-1):
        if magnitudes[num] == magnitudes[num+1] and magnitudes[num] not in magSet:
            magSet.append(magnitudes[num])
            magCount.append(count)
            count += 1
        elif magnitudes[num] == magnitudes[num+1] and magnitudes[num] in magSet:
            count += 1
        elif magnitudes[num] != magnitudes[num+1] and magnitudes[num] not in magSet:
            count += 1
            magSet.append(magnitudes[num])
            magCount.append(count)
            count = 0
        else:
            count += 1
            magCount[len(magCount)-1] = count
            count = 0
    if magnitudes[len(magnitudes)-1] == magnitudes[len(magnitudes)-2] and magnitudes[len(magnitudes)-1] in magSet:
        magCount[len(magCount)-1] += 1
    elif magnitudes[len(magnitudes)-1] != magnitudes[len(magnitudes)-2] and magnitudes[len(magnitudes)-1] not in magSet:
        magSet.append(magnitudes[len(magnitudes)-1])
        magCount.append(1)
    magTup = list(zip(magSet,magCount))
    xMax = magnitudes[len(magnitudes)-1]
    xMin = magnitudes[0]
    printHisto(magTup, xMin, xMax)
        
def startScan(url):
    page = urllib.request.urlopen(url)
    pageText = page.readlines()
    earthquakeCount(pageText)

def printBoard(board):
    grid = [["-" for i in range(len(board))] for i in range(len(board))]
    row = 0
    for item in board:
        grid[row][item] = "Q"
        row += 1
    print("Solved Board!")
    for r in grid:
        for c in r:
            print(c, end=' ')
        print()

def canPlace(board, pos, y):
    for num in range(pos):
        if (board[num] == y) or (abs(num - pos) == abs(board[num] - y)):
            return False
    return True
            
def placeQueen(board, pos, n):
    for num in range(n):
        if canPlace(board, pos, num):
            board[pos] = num
            if pos == n - 1:
                printBoard(board)
            placeQueen(board, pos+1, n)

def nQueens(n):
    board = [None]*n
    print("Below are various solutions to the NQueens Problem")
    placeQueen(board, 0, n)            
        
    

startScan("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv")
nQueens(8)
 
