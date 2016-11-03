my_list = []

def SortList(my_list):
    sort_list =[]
    while my_list:
        lowest_val = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] < lowest_val:
                lowest_val = my_list[i]
        sort_list.append(lowest_val)
        my_list.remove(lowest_val)
    print(sort_list)


            
SortList(my_list)

#the idea from while my_list came from
#http://stackoverflow.com/questions/53513/best-way-to-check-if-a-list-is-empty
#While my_list checks to make sure list exists
#Documentation shows an if statement that has a list that's empty

