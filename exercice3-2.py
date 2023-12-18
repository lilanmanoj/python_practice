#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Loops Tutorial
Exercise 2
"""
num = int(input("Enter number: "))
i = 1
total = 0

while (i <= num):
    total += i
    i = i + 1
    
print("Total is: ", total)