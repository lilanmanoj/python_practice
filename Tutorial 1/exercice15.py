"""
Exercise 15

"""

def printList(lst):
    newList = []
    
    for i in lst:
        newList.append(i)
        
    print(newList)

nameList = ["John Smith", "Michael Anderson", "Archibald Farnsworth the Fourth"]
nameList[1] = "Lilan Manoj"
printList (nameList)