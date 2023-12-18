#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Loops Tutorial
Exercise 6
"""
rows = range(5, 0, -1)

for row in rows:
    cols = range(row, 0, -1)
    
    for col in cols:
        print(col, end = " ")
    
    print("")
