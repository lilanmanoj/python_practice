# -*- coding: utf-8 -*-
"""
Exercise 12

"""

def getInput():
    val = input("Enter number:")
    return val

def checkDividable(n1, n2):
    return (int(n1) % int(n2)) == 0

num1 = getInput()
num2 = getInput()
isDividable = checkDividable(num1, num2)
result = "no"

if (isDividable == True):
    result = "Yes"
else:
    result = "No"

print("Can number 1 divided by number 2: ",result)