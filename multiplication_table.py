num_1 = int(input('Enter Value 1: '))
num_2 = int(input('Enter Value 2: '))

def PrintMultiplicationTable(num_1,num_2):
    for i in range(1, num_1 +1):
        for j in range (1, num_2 +1):
            print (i, 'x', j, '=', i*j)

PrintMultiplicationTable(num_1, num_2)
