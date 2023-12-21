"""
Exercise 20

"""

def checkIsPrimeNumber(n):
    divisorList = []
    i = 1
    
    while (i <= n):
        if (n % i) == 0:
            divisorList.append(i)
        
        i += 1
        
    return len(divisorList) == 2

primeNumberList = []
currentNumber = 2;

while (len(primeNumberList) < 100):
    isPrime = checkIsPrimeNumber(currentNumber)
    
    if (isPrime):
        primeNumberList.append(currentNumber)
        
    currentNumber += 1

print (primeNumberList)