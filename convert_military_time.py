prompt_hour = int(input('Enter the hour:'))
prompt_min = int(input(' Enter the minutes:'))

if prompt_min < 10:
    prompt_min = str(prompt_min)
    prompt_min = '0' + prompt_min
    
if prompt_hour > 12:
    prompt_hour = prompt_hour - 12
    print(prompt_hour ,':', prompt_min , 'PM')
    
elif prompt_hour == 0:
    prompt_hour = prompt_hour + 12
    print(prompt_hour ,':', prompt_min , 'AM')
    
elif prompt_hour <= 12:
    print(prompt_hour ,':', prompt_min , 'AM')
    

