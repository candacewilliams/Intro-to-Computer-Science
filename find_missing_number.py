def FindMissingNumber(sorted_nums):
    min = sorted_nums[0]
    max = sorted_nums[len(sorted_nums)-1]

    for val in sorted_nums:
        if val + 1 not in sorted_nums and val +1 < max and val +1 > min:
            print(val + 1)
    

def SortList(nums):
    sorted_nums = []
    while nums:
        lowest_val = nums[0]
        
        for val in nums: 
            if val < lowest_val:
                lowest_val  =  val
                
        sorted_nums.append(lowest_val)
        nums.remove(lowest_val)
        
    return sorted_nums
    

nums = [45,47]
sorted_nums = SortList(nums)
FindMissingNumber(sorted_nums)
