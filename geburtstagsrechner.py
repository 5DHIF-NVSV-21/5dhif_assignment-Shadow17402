from datetime import date, timedelta
import datetime

def addYears(d, years):
    try:       
        return d.replace(year = d.year + years)
    except ValueError:       
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

_continue = 1
while bool(_continue):
    print('Wann ist ihr Geburtstag?')
    try:
        x = input()
    except ValueError:
        print('Invalid Date')
    _today = date.today()
    year = int(x.split('.')[2])
    month = int(x.split('.')[1])
    day = int(x.split('.')[0])
    bday_date = date(year,month,day)
    if month >= _today.month:
        if day >= _today.day:
            bday_date = addYears(bday_date,_today.year-bday_date.year)
        else:
            bday_date = addYears(bday_date,_today.year-bday_date.year+1)
    else:
            bday_date = addYears(bday_date,_today.year-bday_date.year+1)
    timedelta = bday_date - _today
    if timedelta.days == 0:
        print('Your Birthday is today')
    elif timedelta.days == 1: 
        print('Your Birthday is tomorrow')
    else:
        print('Your Birthday is in ' + str(timedelta.days) + ' Days')
    print('')
    print('Do you want to enter a different Date?')
    _input = input()
    if _input.lower() != 'yes' or _input.lower() != 'y':
        _continue = 0