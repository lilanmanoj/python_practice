#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Conditional Statement Tutorial
Exercise 1
"""

salary = int(input("Enter salary: "))
service = int(input("Enter year of service: "))
bonus = 0;

if service > 5:
    bonus = salary * 5 / 100;
    
print("Bonus is: ", bonus)
print("Net salary is: ", salary + bonus)