#Edgar Ruiz
#CS 299
#Exam 1 Part 2
#October 27th, 2016

#!/usr/bin/python

def tags(L1, L2):
    if(len(L1) == len(L2)):
        maxValue = 0
        for num in range(len(L1)):
            if(L2[num] == -1):
                pass
            else:
                if(L1[num] > maxValue):
                    maxValue = L1[num]
        zipped = []
        for (x,y) in zip(L1, L2):
            zipped.append((x,y))
        zipped.sort()
        print(zipped)
        if(maxValue > 0):
            print("MaxValue is: ", maxValue)
        else:
            print("There is no MaxValue with a tag of 1")

def bankServiceFee(*checks, name, base):
    totalFees = 0.00
    totalChecks = 0
    for check in checks:
        totalChecks += check    
    if(totalChecks >= 51):
        totalFees += 0.10 * 20
        totalChecks -= 20
        totalFees += 0.07 * 30
        totalChecks -= 30
        totalFees += 0.05 * totalChecks
        totalChecks -= totalChecks 
    elif(totalChecks >= 21 and totalChecks <= 50):
        totalFees += 0.10 * 20
        totalChecks -= 20
        totalFees += 0.07 * totalChecks
        totalChecks -= totalChecks
    else:
        totalFees += 0.10 * totalChecks
        totalChecks -= totalChecks
    total = totalFees + float(base)
    print("Total Bank Service Fee for %s is $" % (name), round(total, 2))

bankServiceFee(15,29,18,7, name="Jack", base=10)
bankServiceFee(36, name="Joan", base=10)
bankServiceFee(3,5,2,6, name="David", base=20)
bankServiceFee(name="Diana", base=20)
tags(L1 = [13,3,25,7,21,2,50,2,13,40,34,14,6,16], L2 = [1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,-1])
tags(L1 = [45,21,4,31,2], L2 = [1,1,1,1,1])
tags(L1 = [13,3,45], L2 = [-1,-1,-1])
     
