"""
Exercise 21

"""

def getInput():
    val = input("Enter number:")
    return int(val)

def checkIsPrimeNumber(n):
    divisorList = []
    i = 1
    
    while (i <= n):
        if (n % i) == 0:
            divisorList.append(i)
        
        i += 1
        
    return len(divisorList) == 2

def primes(n):
    primeNumberList = []
    currentNumber = 2;
    
    if (n > 1):
        while (len(primeNumberList) < n):
            isPrime = checkIsPrimeNumber(currentNumber)
            
            if (isPrime):
                primeNumberList.append(currentNumber)
                
            currentNumber += 1
    
    return len(primeNumberList)

n = getInput()
primesCount = primes(n)

print (primesCount)