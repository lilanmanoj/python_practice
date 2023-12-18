#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Conditional Statement Tutorial
Exercise 2
"""

totalClasses = int(input("Enter number of classes held: "))
totalAttended = int(input("Enter number of classes attended: "))
hasMedical = input("Has medical (Enter Y/N): ")

attendencePercentage = totalAttended/totalClasses * 100
canSitExam = "No"

if attendencePercentage >= 75:
    canSitExam = "Yes"
elif attendencePercentage < 75 and hasMedical == "Y":
    canSitExam = "Yes"
    
print("Percentage of class attended: ", attendencePercentage, "%")
print("Allowed to sit exam: ", canSitExam)