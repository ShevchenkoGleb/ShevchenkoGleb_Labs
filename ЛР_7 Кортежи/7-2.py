spisok=[]
repeated_spisok=set()
previous_value = []
for x in range(5):
    a=int(input("Введите число для списка: "))
    spisok.append(a)
sorted_spisok=sorted(spisok)
print(sorted_spisok)

for curr in sorted_spisok:
    if curr == previous_value:
        repeated_spisok.add(curr)
    previous_value = curr
if repeated_spisok:
    print("Повторяющиеся элементы: ", list(repeated_spisok))
else:
    print("Повторяющихся элементов нет.")
