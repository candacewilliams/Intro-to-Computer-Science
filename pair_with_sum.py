
def HasPairWithTargetSum(nums, target_sum):
    if len(nums) == 0:
        print('False')
        return False
    
    else:
        for val in nums:
            for num in nums[1:]: 
                if val + num == target_sum:
                    print('True')
                    return True
                         
        print('False')
        return False 
        


nums = [3,3]
target_sum = 6

HasPairWithTargetSum(nums, target_sum)
#works for every case but 2,2,3 target sum = 6
