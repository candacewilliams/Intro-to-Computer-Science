val_list = [10,-1,-1,10]


def IsPalindrome (val_list):
    for i in range(len(val_list)):
        original = val_list[i]
        for j in range(len(val_list)-1,-1,-1):
            reverse = val_list[j]
    if original == reverse:
        print('True')
    else:
        print('False')
            
IsPalindrome(val_list)
