def AreStringsSimilar(str_1, str_2):
    diff_char = 0
    char_1 = 0
    char_2 = 0
    
    if len(str_1) == len(str_2):
        for char in range(len(str_1)):
            if str_1[char] != str_2[char]:
                diff_char += 1
            if diff_char > 1:
                print('False')
        print('True')
                
    elif abs(len(str_1) - len(str_2)) > 1:
        print('False')

    elif len(str_1) != len(str_2) and abs(len(str_1) - len(str_2)) == 1:
        for char in range(len(str_1)):
            if str_1[char] == str_2[char]:
                char_1 += 1
                char_2 += 1
                
            if str_1[char] != str_2[char]:
                diff_char += 1
                char_1 += 1
            
            if diff_char > 1:
                print('False')
                break
            
        if diff_char == 0:
            print('True')
               
            
    elif len(str_1) != len(str_2) and abs(len(str_1) - len(str_2)) != 1:
        for char in range(len(str_1)):
            if str_1[char] == str_2[char]:
                char_1 += 1
                char_2 += 1
                
            if str_1[char] != str_2[char]:
                diff_char += 1
                char_1 += 1
            
            if diff_char > 1:
                print('False')
                break
            
    elif abs(len(str_1) - len(str_2)) == 1:
        print('True')                   
        

str_1 = input('Enter First String :')
str_2 = input('Enter Second String :')


AreStringsSimilar(str_1, str_2)
