"""
Exercise 19

"""
def getInput():
    val = input("Enter number:")
    return int(val)

def getDivisorsList(l, n):
    newList = []
    
    for i in l:
        if n % i == 0:
            newList.append(i)
            
    return newList

n = getInput()
dividorList = range(1, n + 1)
divisorList = getDivisorsList(dividorList, n)

print (divisorList)