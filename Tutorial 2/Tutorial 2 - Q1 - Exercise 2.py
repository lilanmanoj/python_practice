#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Conditional Statement Tutorial
Exercise 2
"""

quantity = int(input("Enter quantity: "))
unitCost = 100
discount = 0
cost = quantity * unitCost

if quantity > 1000:
    discount = cost * 10 / 100;

totalCost = cost - discount
    
print("Your total cost is: ", totalCost)