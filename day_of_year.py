month = input('Insert Month: ')
day = int(input('Insert Day: '))

def GetDayOfYear(month,day):
    if month == 'January':
        print(day)
    if month == 'February':
        print(day + 31)
    if month == 'March':
        print(day +(31 + 28))
    if month == 'April':
        print(day + ((31*2) + 28))
    if month == 'May':
        print(day + ((31*2) + 30 + 28))
    if month == 'June':
        print(day + ((31*3) + 30 + 28))
    if month == 'July':
        print(day + ((31*3) + (30*2) + 28))
    if month == 'September':
        print(day +(31*4) + (30*2) + 28)
    if month == 'October':
        print(day + (31*5) + (30*3) + 28)
    if month == 'November':
        print(day + (31*6) + (30*3) + 28)
    if month == 'December':
        print(day + (31*6) + (30*4) + 28)

GetDayOfYear(month, day)


