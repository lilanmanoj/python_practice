#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Loops Tutorial
Exercise 8
"""
totalRows = int(input("Enter total rows: "))

if (totalRows % 2 != 0):
    totalRows = totalRows + 1

halfRows = (totalRows / 2) + 1
rows = range(1, totalRows, 1)
decrementVal = 2

for row in rows:
    if (row < halfRows):
        starCount = row
        stars = range(starCount, 0, -1)
        
    else:
        starCount = (row - decrementVal) + 1
        stars = range(1, starCount)

        decrementVal = decrementVal + 2
    
    for star in stars:
        print("*", end = " ")
    
    print("")
