nums = [2, 4, 6, 5, 3, 1]


def GetSecondLargestNumber(nums):
    if len(nums)<= 1:
        print('None')
    else:
        largest_num = nums[0]
        second_largest = nums[0]
        for i in nums:
            if largest_num < i:
                largest_num = i
                nums.remove(i)
                second_largest = largest_num
        print(second_largest)
            
        
GetSecondLargestNumber(nums)


#-2,-2,-3,-2 case does NOT work
