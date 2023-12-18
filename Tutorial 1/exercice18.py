"""
Exercise 18

"""
def getInput():
    val = input("Enter n:")
    return int(val)

def cumulativeSum(l):
    return sum(l)

n = getInput()
nums = range(0, n)
cumSum = cumulativeSum(nums)

print (cumSum)