nums = [1,2.5,3,3,4,4,4]
def PrintHistogram(nums):
    num_stars = 0
    GetStars(nums, num_stars)
    
def PrintStars(num_stars):
    for num in range(num_stars):
        print('*', end = '')
    print('\n')

def GetStars(nums, num_stars):
    for val in nums:
        if val != nums[nums.index(val)+1]: 
            num_stars = 1
            print(val , ':' , end = '')
            PrintStars(num_stars)
            num_stars = 0
            
        elif val == nums[nums.index(val)+1]:   
            num_stars +=1
            print(val , ':' , end = '')
            PrintStars(num_stars)
            num_stars = 0
            
        

    
PrintHistogram(nums)
#Documentation: http://stackoverflow.com/questions/2167868/getting-next-element-while-cycling-through-a-list


