def GetIntersectionSize(range_1_min, range_1_max, range_2_min, range_2_max):
    '''
    This function should return the intersection size of the two ranges.
    Replace the line below with the correct code.
    '''
   
    if (range_2_min > range_1_max):
        intersection_size = -1

    elif ((range_1_min == range_1_max) or (range_2_min == range_2_max)):
        intersection_size = 0

    elif ((range_2_min > range_1_min) and (range_2_max > range_1_max)):
        intersection_size =(range_1_max - range_2_min)

    elif ((range_2_min > range_1_min) and (range_2_max < range_1_max)):
        inersection_size =(range_2_max - range_2_min)
        
    return intersection_size
    
'''
partner-programmed with Ivey Hill.
I don't know what I should write other than that.
I just felt weird because the variables were pre-made so our code will look similar.
Since I've never worked with anyone like this, I'm not sure what qualifies as cheating.
'''
    
# You don't need to change anything below this line.
range_1_min = int(input('Enter the min number for range 1: '))
range_1_max = int(input('Enter the max number for range 1: '))
range_2_min = int(input('Enter the min number for range 2: '))
range_2_max = int(input('Enter the max number for range 2: '))


intersection_size = GetIntersectionSize(
    range_1_min, range_1_max, range_2_min, range_2_max)
print('The intersection size is', intersection_size)
