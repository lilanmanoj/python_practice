# -*- coding: utf-8 -*-
"""
Exercise 13

"""

def multiplyEach(l, n):
    newList = []
    
    for i in l:
        newList.append(i * n)
    
    return newList

def diffList(l1, l2):
    newList = []
    i = 0

    while i < len(l1):
        diff = l2[i] - l1[i]
        newList.append(diff)
        i += 1
        
    return newList

list1 = [ 1, 2, 3, 4, 5]
list2 = multiplyEach(list1, 9)
list3 = diffList(list1, list2)

print ("Original list is: ", list1)
print ("Multiplied list is: ", list2)
print ("Subtracted list is:", list3)