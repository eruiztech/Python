#Edgar Ruiz
#CS 299
#Lab 5
#October 20th, 2016

#!/usr/bin/python

import urllib.request

def findHigh(high):
    highest = float(high[0])
    index = 0
    count = 0
    for item in high:
        if float(item) >= highest:
            index = count
            count += 1
        else:
            count += 1
    return index, round(float(high[index]), 2)
    
def findLow(low):
    lowest = float(low[0])
    index = 0
    count = 0
    for item in low:
        if float(item) <= lowest:
            index = count
            count += 1
        else:
            count += 1
    return index, round(float(low[index]), 2)

def findVolume(volume):
    largest = int(volume[0])
    index = 0
    count = 0
    for item in volume:
        if int(item) >= largest:
            index = count
            count += 1
        else:
            count += 1
    return index, int(volume[index])

def findClose(close):
    averageClose = 0
    for item in close:
        averageClose += float(item)
    averageClose = float(averageClose / 5)
    return round(averageClose, 2)

def splitData(pageText):
    friday = str(pageText[4]).split(",")
    thursday = str(pageText[5]).split(",")
    wednesday = str(pageText[6]).split(",")
    tuesday = str(pageText[7]).split(",")
    monday = str(pageText[8]).split(",")

    week = [monday, tuesday, wednesday, thursday, friday]
    weekDay = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    date = []
    Open = []
    high = []
    low = []
    close = []
    volume = []

    for num in range(5):
        day = week[num]
        date.append(day[0])
        Open.append(day[1])
        high.append(day[2])
        low.append(day[3])
        close.append(day[4])
        volume.append(day[5])

    highest = findHigh(high)
    print(weekDay[highest[0]], ", share price is $", highest[1], ", the highest of the week.")
    lowest = findLow(low)
    print(weekDay[lowest[0]], ", share price is $", lowest[1], ", the lowest of the week.")
    largestVolume = findVolume(volume)
    print("Highest trading volume is", largestVolume[1], "shares, happended on", weekDay[largestVolume[0]])
    averageClose = findClose(close)
    print("This week's average closing price is $", averageClose)

def highTrade(pageText):
    date = []
    highList = []
    temp = []
    for num in range(5219): #10-20-1976 to 10-20-2016
        temp = str(pageText[num+1]).split(",")
        date.append(temp[0][2:])
        highList.append(int(temp[5]))

    highTradeVol = highList[0]
    index = 0
    count = 0
    for num in highList:
        if num >= highTradeVol:
            highTradeVol = num
            index = count
            count += 1
        else:
            count += 1
    return highTradeVol, date[index]
    
def startScan(url):
    page = urllib.request.urlopen(url)
    pageText = page.readlines()
    splitData(pageText)
    highestTrade = highTrade(pageText)
    print("The highest trading volume of the last 20 years is:", highestTrade[0], ", which happened on", highestTrade[1]) 

print("Data for Target")
startScan("https://chart.yahoo.com/table.csv?s=TGT")
print("Data for Microsoft")
startScan("https://chart.yahoo.com/table.csv?s=MSFT")

