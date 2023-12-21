# -*- coding: utf-8 -*-
"""
Exercise 7

"""

import math

a = int(input ("Enter length of first side of the triangle: "))
b = int(input ("Enter length of second side of the triangle: "))
angle = int(input ("Enter angle between the above sides of that triangle (In degrees): "))

area = 1/2 * a * b * math.sin(angle * math.pi / 180)

print ("Area of the triangle is", round(area, 2))
