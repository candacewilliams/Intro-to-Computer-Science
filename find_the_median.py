
val_1 = int(input('Enter Value One: '))
val_2 = int(input('Enter Value Two: '))
val_3 = int(input('Enter Value Three: ')) #14,3,27  10,20,20  10,20, 10


if val_1 >= val_2 :
    new_val_1 = val_2
else:
    new_val_1 = val_1
            
if val_2 >= val_3 : 
    new_val_2 = val_3
else:
    new_val_2 = val_1
    
if val_1 >= val_3 :
    new_val_3 = val_3
else:
    new_val_3 = val_2


print('The middle number is ' , new_val_2)
