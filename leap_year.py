year = int(input('Enter Year: '))


def IsLeapYear(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('True')
    else:
        print('False') 

IsLeapYear(year)
