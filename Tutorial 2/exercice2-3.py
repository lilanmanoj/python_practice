#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Conditional Statement Tutorial
Exercise 2
"""

marks = int(input("Enter marks: "))
grade = "F"

if marks > 80:
    grade = "A"
elif marks > 60 and marks <= 80:
    grade = "B"
elif marks > 50 and marks <= 60:
    grade = "C"
elif marks > 45 and marks <= 50:
    grade = "D"
elif marks > 25 and marks <= 45:
    grade = "E"
    
print("Your grade is: ", grade)