#Edgar Ruiz
#CS 299
#Lab 3 Problem 2
#Due: October 6th, 2016

#!/usr/bin/python

print("Lab 3\nSales Receipt Problem\n")

def salesReceiptPrint(*itemCost, taxRate = 0.08):
	subTotal = 0.0
	print("Item costs")
	for item in itemCost:
		print("$", item)
		subTotal += item
	print("Tax rate: ", round(float(taxRate * 100), 2), "%")
	print("Subtotal: $", round(subTotal,2))
	subTax = subTotal * taxRate
	print("Subtotal w/ tax: $", round(subTax, 2))
	total = round((subTax) + subTotal, 2)
	return total

print("Total is: $", salesReceiptPrint(80, 125, 45.5), "\n")
print("Total is: $", salesReceiptPrint(95, taxRate = 0.105), "\n")
print("Total is: $", salesReceiptPrint(12, 5.5, 6.5, 7.5, 9.0, taxRate = 0.07), "\n")
