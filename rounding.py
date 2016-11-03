num = int(input('Enter Number :'))
n = int(input('Enter Multiple :'))

def RoundNumToNearestMultiple(num, n):
        temp_val = num / n
        round_val =(round(temp_val))
        round_val = round_val * n
        print(round_val)

RoundNumToNearestMultiple(num, n)
