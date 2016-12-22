def CombineTwoSortedLists(list_1, list_2):
    combined_list = []
    sorted_list = []

    for i in list_1:
        combined_list.append(i)
    
    for j in list_2:
        combined_list.append(j)

    while combined_list:
        lowest_val = combined_list[0]
        
        for val in combined_list: 
            if val < lowest_val:
                lowest_val  =  val
                
        sorted_list.append(lowest_val)
        combined_list.remove(lowest_val)
        
    print(sorted_list)

    

list_1 = [6]
list_2 = [1,2]

CombineTwoSortedLists(list_1, list_2)
