"""
Exercise 16

"""

def square(l):
    newList = []
    
    for i in l:
        newList.append(i ** 2)
        
    return newList

nums = range(1, 11)
squared = square(nums)
print (squared)