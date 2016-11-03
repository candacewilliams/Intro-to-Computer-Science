start = int(input('Enter First Number: '))
end = int(input('Enter Last Number: '))
multiple = int(input('Enter Multiple Value: '))


def PrintMultiples(start, end, multiple):
    if multiple <= 0 :
        print('Input multiple must be greater than 0')

    elif end % multiple == 0:
        print(end)
        
    if end < start :
        swap_end = start
        swap_start = end
        start = swap_start
        end = swap_end
        
        #make start value the end value
        #make end value the start value
        
    if multiple > 0:
        mult_list = False
        for i in range(start,end):
            if i % multiple == 0:
                 mult_list = True
                 print(i)
        if start == end:
            mult_list = True 
        if mult_list == False:
            print('There are no multiples' , multiple, 'in the range' , start , 'to',  end)
    
             
PrintMultiples(start, end, multiple)
