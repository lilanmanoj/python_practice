#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:32 2023

@author: lilanmanoj

Python Loops Tutorial
Exercise 5
"""
i = 1

while (i <= 5):
    n = 1
    
    while (n <= i):
        print(n, end = " ")
        n = n + 1
    
    print("")
    i = i + 1
