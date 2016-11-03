minutes = float(input('Minutes: '))

num_hours = float(minutes / 60)
num_hours = int(num_hours)
#print(num_hours)

num_minutes = float(minutes % 60)
whole_minutes = int(num_minutes)
#print(num_minutes)

num_seconds = minutes - int(minutes)
num_seconds = num_seconds * 60
num_seconds = round(num_seconds)

print(num_hours , 'hours,' , whole_minutes , 'minutes,' , num_seconds , 'seconds')
