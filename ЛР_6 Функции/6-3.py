from datetime import datetime
def magic_date(date_stroka):
    try:
        date=datetime.strptime(date_stroka,'%d.%m.%Y')
        day=date.day
        month=date.month
        year=date.year
        if day*month==year%100:
            return True
        else:
            return False
    except ValueError:
        print("Введите верно дату (дд.мм.гггг.)")
        return

vvod_usera=input("Введите дату: ")
if magic_date(vvod_usera)==True:
    print("Дата является магической")
else:
    print("Дата не является магической")