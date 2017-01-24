#Edgar Ruiz
#CS 299
#Exam 2 Part 2
#November 22, 2016

#!/usr/bin/python

class emptyException(Exception):
    pass
class removeNonNum(Exception):
    pass

class BinaryNumber:
    def __init__(self, binNum):
        #try:
        if len(binNum) == 0:
                #raise emptyException()
            binNum = '0'
        
        newbinNum = ''
        for x in binNum:
            if x == '0' or x == '1':
                newbinNum += x
                    #raise removeNonNum()
        self.binNum = newbinNum
        #except emptyException:
            #pass
        #except removeNonNum:
        #    pass
    def value(self):
        integer = 0
        count = 0
        for x in self.binNum[::-1]:
            integer += int(x) * (2**count)
            count += 1
        return integer

b1 = BinaryNumber('11101')
print(BinaryNumber.value(b1))
b2 = BinaryNumber('')
print(BinaryNumber.value(b2))
b3 = BinaryNumber('01E1310x1')
print(BinaryNumber.value(b3))
b4 = BinaryNumber('E3x5k')
print(BinaryNumber.value(b4))
