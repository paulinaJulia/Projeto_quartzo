from datetime import datetime, timedelta


def days_of_month(date: datetime):
    if date.month == 1:
        return 31
    if date.month == 2:
        return 29 if date.year % 4 == 0 else 28
    if date.month == 3:
        return 31
    if date.month == 4:
        return 30
    if date.month == 5:
        return 31
    if date.month == 6:
        return 30
    if date.month == 7:
        return 31
    if date.month == 8:
        return 31
    if date.month == 9:
        return 30
    if date.month == 10:
        return 31
    if date.month == 11:
        return 30
    if date.month == 12:
        return 31


def dates(date: datetime, limited):
    date = date + timedelta(days=days_of_month(date))
    i = 0
    dates = []
    while i < limited:
        if i > 0:
            date = date + timedelta(days=days_of_month(date))
        i += 1
        dates.append(date)

    return dates
    
for date in dates(datetime.now(), 24):


    """
        imprimir a lista de datas 
    for date in dates(datetime.now(), 24):
        print(date)"""