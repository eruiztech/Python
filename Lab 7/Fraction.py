#Edgar Ruiz
#CS 299
#Lab 7
#November 10th, 2016

#!/usr/bin/python

class Fraction:
    def __init__(self, numerator, denominator):
        simplified = self.simplify(numerator, denominator)
        self.numerator = simplified[0]
        self.denominator = simplified[1]
    def getNum(self):
        return self.numerator
    def getDenom(self):
        return self.denominator
    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator),
        else:
            tempDnum1 = self.denominator * other.denominator
            tempNum1 = self.numerator * other.denominator
            tempNum2 = other.numerator * self.denominator
            return Fraction(tempNum1 + tempNum2, tempDnum1)
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
    def __lt__(self, other):
        return (self.numerator / self.denominator) < (other.numerator / other.denominator)
    def simplify(self, num, denom):
        factor = 1
        for i in range(min(num, denom), 1, -1):
            if num % i == 0 and denom % i == 0:
                factor = i
                break
        newNum = num / factor
        newDenom = denom / factor
        return int(newNum), int(newDenom)
    
test1 = Fraction(2, 15) + Fraction(1, 5)
print("2 / 15 + 1 / 5 =", test1.getNum(), "/", test1.getDenom())
test2 = Fraction(3, 14) + Fraction(4, 7)
print("3 / 14 + 4 / 7 =", test2.getNum(), "/", test2.getDenom())
test3 = Fraction(2, 15) * Fraction(3, 4)
print("2 / 15 * 3 / 4 =", test3.getNum(), "/", test3.getDenom())
test4 = Fraction(5, 7) * Fraction(4, 35)
print("5 / 7 * 4 / 35 =", test4.getNum(), "/", test4.getDenom())
print("2 / 15 == 4 / 25?", Fraction(2, 15) == Fraction(4, 25))
print("2 / 15 == 4 / 30?", Fraction(2, 15) == Fraction(4, 30))
print("2 / 15 < 4 / 25?", Fraction(2, 15) < Fraction(4, 25))
print("9 / 15 < 7 / 12?", Fraction(9, 15) < Fraction(7, 12))
