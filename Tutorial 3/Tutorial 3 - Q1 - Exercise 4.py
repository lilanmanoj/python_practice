#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Loops Tutorial
Exercise 4
"""
numbers = [12, 75, 150, 180, 145, 525, 50]
passed = []

for num in numbers:
    if num > 500:
        break
    
    if num > 150 and num < 500:
        continue
    
    if num % 5 == 0:
        passed.append(num)
        
print ("Satisfied numbers: ", passed)