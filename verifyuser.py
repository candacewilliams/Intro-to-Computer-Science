def VerifyUser(user_info,username_input,password_input):
    
    for val in user_info:
        user_one = user_info[0]
        user_two = user_info[1]
        
        for user_name in user_one:
            if username_input == user_one[0]:
                if password_input == user_one[1]:
                        print('True')
                        break
        for user_name in user_two:
            if username_input == user_two[0]:
                if password_input == user_two[1]:
                    print('True')
                    break
        break




username_input = input('Enter Username :')
password_input = input('Enter Password :')
user_info = [['mking2016', 'hackath0n', 'Matthew King', '1234567887654321', '500'], ['jwalk2016', 'walking', 'Jessica Walker', '8765432112345678', '550']]
VerifyUser(user_info,username_input, password_input)

