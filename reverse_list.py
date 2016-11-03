num_list = [1,2,3,4]

def ReverseList(num_list):
    reverse_list = []
    print (num_list)
    for num in range(len(num_list)-1,-1,-1):
    #start at last index
        reverse_list.append(num_list[num])
    print(reverse_list)

ReverseList(num_list)
