#this code is trash tbh. I finna turn it in tho.
#It really doesn't work, but I tried.
#It kinda works for a list of only ints, but not really
#RIP  ¯\_(ツ)_/¯

def SortByFrequency(vals):
    vals_dict = {}
    sorted_vals = SortList(vals)
    print(sorted_vals)
    
    for val in sorted_vals:
        if val not in vals_dict:
            vals_dict[val] = 0
            
        if val in vals_dict:
            vals_dict[val] = vals_dict[val] + 1
            
    print(vals_dict)
    PrintNumTimes(vals_dict)

def PrintNumTimes(vals_dict):
    num_times = 0
    
    for j in vals_dict:
        max_key = max(vals_dict, key = vals_dict.get)
        if j == max_key:
            num_times = vals_dict[j]
            
            for h in range(num_times):
                print(j , end = '')
            vals_dict[j] = 0
            
            
def SortList(vals):
    sorted_vals = []
    while vals:
        lowest_val = vals[0]
        for i in vals: 
            if i < lowest_val:
                lowest_val  =  i
                
        sorted_vals.append(lowest_val)
        vals.remove(lowest_val)
        
    return sorted_vals

vals = [2,3,2,1,1,2]
SortByFrequency(vals)
