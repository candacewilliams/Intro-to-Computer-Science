nums = [5, 4, 3, 4, 5, 6, 7, 6, 5]

def PrintHistogram(nums):
    my_dict = {}
    
    for val in nums:
        if val not in my_dict:
            my_dict[val] = 1
            
        elif val in my_dict:
            my_dict[val] = my_dict[val] + 1
            
    PrintStars(my_dict)

def PrintStars(my_dict):
    for key in my_dict:
        print(key, ':' , end = '')
        num_stars = my_dict[key]
        
        for num in range(num_stars):
            print('*', end = '')
        print('\n')
    
    
PrintHistogram(nums)
    
