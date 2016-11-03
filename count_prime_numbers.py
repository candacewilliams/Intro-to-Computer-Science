nums = [27281,23547,23549,23551,41661]


def IsNumberPrime(nums):
    for i in range (2, nums):
        if nums % i == 0:
            return False
        return True

def CountPrimeNumber(nums):
    num_prime = 0
    for i in nums:
        if i == 2:
            num_prime +=1
        elif (i>0)and(IsNumberPrime(i)== True):
            num_prime += 1
    print(num_prime)
        
    
    
       
CountPrimeNumber(nums)
