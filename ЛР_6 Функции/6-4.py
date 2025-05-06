'''def check_lucky_ticket():
    """
    Функция, проверяющая является ли номер счастливым
    """
    print("Введите номер билета: ")
    a = [int(i) for i in input()]
    if len(a) % 2 != 0:
        print("В билете должно быть четное количество цифр")
        check_lucky_ticket()
        return
    if sum(a[:int(len(a)/2)]) == sum(a[int(len(a)/2):]):
        print("Счастливый билет")
    else:
        print("Не счастливый билет")


if __name__ == '__main__':
    check_lucky_ticket()'''

def check_ticket(ticket_numb):
    if len(ticket_numb)%2!=0:
        print("Кол-во цифр в билете должно быть чётно")
        return

    half=len(ticket_numb) // 2
    first_half_sum = sum(map(int, ticket_numb[:half]))
    second_half_sum = sum(map(int, ticket_numb[half:]))

    if first_half_sum == second_half_sum:
        print("Билет счастливый!")
    else:
        print("Билет не счастливый.")
ticket=input("Введите билет: ")
check_ticket(ticket)