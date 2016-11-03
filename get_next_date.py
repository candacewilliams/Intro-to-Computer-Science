month = int(input('Enter Month: '))
day = int(input('Enter Day: '))
year = int(input('Enter Year: '))


def GetNextDate(month, day, year):
    if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8)or (month == 10)): #months with 31 days excluding December
                  if day != 31:
                      day = day + 1
                      print (str(month) + '/' + str(day) + '/' + str(year))
                  else:
                      month = month + 1
                      day = 1
                      print (str(month) + '/' + str(day) + '/' + str(year))
                      
    elif ((month == 4) or (month == 6) or (month == 9)or (month == 11)): #months with 30 days
                  if day != 30:
                      day = day + 1
                      print (str(month) + '/' + str(day) + '/' + str(year))
                  else: 
                      month = month + 1
                      day = 1
                      print (str(month) + '/' + str(day) + '/' + str(year))
                  
    elif month == 2:
                  if day != 28:
                      day = day + 1
                      print (str(month) + '/' + str(day) + '/' + str(year))
                  else:
                      month = month +1
                      day = 1
                      print (str(month) + '/' + str(day) + '/' + str(year))
    elif month == 12:
                  if day != 31:
                      day = day +1
                      print (str(month) + '/' + str(day) + '/' + str(year))
                  else:
                      month = 1
                      day = 1
                      year = year + 1
                      print (str(month) + '/' + str(day) + '/' + str(year))
                  

GetNextDate(month, day, year)                      
                  
