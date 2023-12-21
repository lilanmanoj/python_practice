# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Loops Tutorial
Exercise 7
"""
given = 76542
digits = []

for i in str(given):
    digits.append(int(i))
    
lastIdx = len(digits)

i = 0

while (i < lastIdx):
    idx = lastIdx - i - 1
    print(digits[idx], end = "")
    i = i + 1