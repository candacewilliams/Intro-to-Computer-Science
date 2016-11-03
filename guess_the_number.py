def GuessTheNumber(mystery_num):
    num_guess = 1
    user_guess = int(input('Enter a guess :'))
    if user_guess == mystery_num:
        print('You\'re correct! It took you' , num_guess, 'guess!')
    while user_guess != mystery_num:
        if user_guess < mystery_num:
            print('Too low!')
            user_guess = int(input('Enter a guess :'))
            num_guess +=1
        
        elif user_guess > mystery_num:
            print('Too high!')
            user_guess = int(input('Enter a guess :'))
            num_guess +=1
    if num_guess > 1:
        print('You\'re correct! It took you' , num_guess , 'guesses!')
        
    
        
        
mystery_num = -1
GuessTheNumber(mystery_num)
    
