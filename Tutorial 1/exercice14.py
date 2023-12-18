"""
Exercise 14

"""

def printList(lst):
    newList = []
    
    for i in lst:
        newList.append(i)
        
    print(newList)

l1 = range(2, 23, 2)
printList (l1)