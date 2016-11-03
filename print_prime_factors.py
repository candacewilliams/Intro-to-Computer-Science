def PrintPrimeFactors(num):
    factors = []
    base_div = 2
    
    while base_div **2 <= num:
        while (num % base_div) == 0:
            factors.append(base_div)
            num //= base_div
        base_div += 1
        
    if num > 1:
       factors.append(num)
    print(factors)
    
    if num <= 1:
        print('There are no factors for' , num)

num = int(input('Enter Value :'))
base_div = 2
#base_div is the check to see if num%2 == 0


PrintPrimeFactors(num)
