
def GetEvenNumOccurrences(my_list, my_dict):
    for char in my_list:
        if char not in my_dict:
            my_dict[char] = 1
            
        elif char in my_dict:
            for char in my_list:
                for char_2 in my_list[1:]:
                    if char == char_2:
                        my_dict[char] = my_dict[char] + 1
                    my_list = [x for x in my_list if x != char]
            return my_dict
    



def PrintEvenOccurrences(my_dict):
    even_list =[]
    for val in my_dict:
        if my_dict[val] %2 == 0:
            even_list.append(val)
    print(even_list)
            
    
my_list = ['fa', 'la', 'pa', 'la', 'fa']
my_dict = {}

GetEvenNumOccurrences(my_list, my_dict)
PrintEvenOccurrences(my_dict)

#works for every case but [1, 1, 1, 2, 2, 2, 2, 3, 3]
#Documentation:http://stackoverflow.com/questions/6148619/start-index-for-iterating-python-list
