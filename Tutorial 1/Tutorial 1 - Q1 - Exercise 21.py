"""
Exercise 21

"""

def getInput():
    val = input("Enter number:")
    return int(val)

def checkIsPrimeNumber(n):
    divisorList = []
    i = 2
    
    if (n >= 2):
        while (i <= n):
            if (n % i) == 0:
                divisorList.append(i)
            
            i += 1
        
    return len(divisorList) == 1

def primesLessThan(n):
    primeNumberList = []
    
    if (n > 1):
        for num in range(1,n):
            isPrime = checkIsPrimeNumber(num)
            
            if (isPrime):
                primeNumberList.append(num)
    
    return primeNumberList

n = getInput()
primes = primesLessThan(n)

print ("Prime numbers count:", len(primes), sep = "\n", end = "\n\n")
print ("Prime numbers:", primes, sep = "\n", end = "\n")
