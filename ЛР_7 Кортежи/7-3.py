days=("Пн","Вт","Ср","Чт","Пт","Cб","Вс")
weekend_days=[]
choice=int(input("Сколько выходных на неделе вы хотите: "))
if choice < 0 or choice > 7:
    print("Пожалуйста, введите число от 0 до 7.")
elif choice > 0 and choice < 8:
    weekend_days = days[-choice:]
    work_days = days[:-choice]
    print(f"Ваши выходные дни: {' '.join(weekend_days)}")
    print(f"Ваши рабочие дни: {' '.join(work_days)}")
elif choice == 0:
    weekend_days = []
    work_days =  days
    print(f"Ваши выходные дни: {' '.join(weekend_days)}")
    print(f"Ваши рабочие дни: {' '.join(work_days)}")
