def IsAnagram(str_1, str_2):
    count = 0
    str1_dict = {}
    str2_dict = {}
    
    for char in str_1:
        if char is not str1_dict:
            count = str_1.count(char)
            str1_dict[char] = count
        if ' ' in str1_dict:
            del str1_dict[' ']
            
            
    for char in str_2:
        if char is not str2_dict:
            count = str_2.count(char)
            str2_dict[char] = count
            
        if char == ' ':
            del str2_dict[' ']
    
    if str1_dict == str2_dict:
        print('True')
    else:
        print('False')
        

str_1 = input('Enter String :')
str_2 = input('Enter String :')

IsAnagram(str_1, str_2)
