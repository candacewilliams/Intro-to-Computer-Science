birth_month = input('Enter Birth Month :')
birth_day = int(input('Enter Birth Day :'))


def GetZodiacSign(birth_month, birth_day):
    if ((birth_month == 'march') and (birth_day >= 21)):
        print('aries')
    elif((birth_month == 'april') and (birth_day <= 19)):
        print('aries')              
    elif((birth_month == 'april') and (birth_day >=20)):
        print('taurus') 
    elif((birth_month == 'may') and (birth_day >= 20)):
        print('taurus')           
    elif((birth_month == 'may') and (birth_day >= 21)):
        print('gemini')
    elif((birth_month == 'june') and (birth_day <= 20)):
        print('gemini')
    elif((birth_month == 'june') and (birth_day >= 21)):
        print('cancer')            
    elif((birth_month == 'july') and (birth_day <= 22)):
        print('cancer')
    elif((birth_month == 'july') and (birth_day <= 23)):
        print('leo')
    elif((birth_month == 'august') and (birth_day <= 22)):
        print('leo')
    elif((birth_month == 'august') and (birth_day >= 23)):
        print('virgo')
    elif((birth_month == 'september') and (birth_day <= 22)):
        print('virgo')
    elif((birth_month == 'september') and (birth_day >= 23)):
        print('libra')
    elif((birth_month == 'october') and (birth_day <= 22)):
        print('libra')
    elif((birth_month == 'october') and (birth_day >= 23)):
        print('scorpio')
    elif((birth_month == 'november') and (birth_day <= 21)):
        print('scorpio')
    elif((birth_month == 'november') and (birth_day >= 22)):
        print('sagittarius')
    elif((birth_month == 'december') and (birth_day <= 21)):
        print('sagittarius')
    elif((birth_month == 'decemeber') and (birth_day >= 22)):
        print('capricorn')
    elif((birth_month == 'january') and (birth_day <= 19)):
        print('Capricorn')
    elif((birth_month == 'january') and (birth_day >= 21)):
        print('aquarius')
    elif((birth_month == 'february') and (birth_day <= 18)):
        print('aquarius')
    elif((birth_month == 'february') and (birth_day >= 19)):
        print('pisces')
    elif((birth_month == 'march') and (birth_day <=20)):
        print('pisces')

GetZodiacSign(birth_month, birth_day)
