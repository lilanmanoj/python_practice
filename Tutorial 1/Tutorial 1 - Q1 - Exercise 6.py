# -*- coding: utf-8 -*-
"""
Exercise 6

"""

import math

num = int(input ("Enter number: "))

if (num > 0):
    log = math.log(num)

    print ("Natural logarithm of the number is", log)
else:
    print ("Entered number is not a positive integer,")
    print ("please enter positive integer to calculate natural logrithm.")
