#Edgar Ruiz
#CS 299
#Lab 6
#Due: November 3rd, 2016

#!/usr/bin/python

def getScore(name, diction):
    try:
        return diction[name]
    except KeyError:
        print("Error, name not found in dictionary")
        return -1

def getMedianScore(diction):
    medList = []
    for key in diction.keys():
        medList.append(diction[key])
    medList.sort()
    if len(medList) % 2 == 0:
        leftMed = int(len(medList) / 2)
        rightMed = int(leftMed - 1)
        med = float((medList[leftMed] + medList[rightMed]) / 2)
        return med
    else:
        medianIndex = int(len(medList) / 2)
        med = medList[medianIndex]
        return med

def scoreDict(diction):
    diction.update({'john':19})
    diction.update({'sue':20}) #Sue's score will update from 18 to 20
    diction['sally'] = 19
    del diction['tom']
    for key in sorted(diction.keys()):
        print(key, diction[key])
    
def makeDict(Names, Scores):
    return dict(zip(Names, Scores))


Names = ['joe', 'tom', 'barb', 'sue', 'sally']
Scores = [10, 17, 20, 18, 15]
Ages = [20, 17, 19, 18, 22]
diction = makeDict(Names, Scores)
print("Dictionary", diction)
s = set(zip(Names, Scores))
fs = frozenset(zip(Names, Ages))
print("Set of Names and Scores tuples: ", s)
print("Frozenset of Names and Ages tuples: ", fs)
print("Intersection of set and frozenset", s & fs)
print("Updating dictionary")
scoreDict(diction)
print("Median of updated dictionary: ", getMedianScore(diction))
print("Retrieving score for barb")
print(getScore('barb', diction))
print("Retrieving score for ana")
print(getScore('ana', diction))

