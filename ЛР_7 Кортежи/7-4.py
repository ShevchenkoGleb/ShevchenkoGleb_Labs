import random
group_1 = [
    "Смирнов", "Иванов", "Петров", "Сидоров", "Кузнецов",
    "Васильев", "Попов", "Михайлов", "Фёдоров", "Николаев"
]

group_2 = [
    "Соловьев", "Андреев", "Ковалев", "Лебедев", "Григорьев",
    "Романов", "Орлов", "Захаров", "Белов", "Егоров"
]

random_group_1 = random.sample(group_1, 5)
print(random_group_1)
random_group_2 = random.sample(group_2, 5)
print(random_group_2)
random_team = random_group_1 + random_group_2
team = tuple(random_team)
print(team)

print("Группа 1:", group_1)
print("Группа 2:", group_2)
print("Спортивная команда:", team)


print("Длина команды:", len(team))


srt=list(team)
sorted_team = sorted(srt)
print("Отсортированная команда по алфавиту:", sorted_team)

student_to_check = "Иванов"
count = team.count(student_to_check)

if student_to_check in team:
    print(f"Студент '{student_to_check}' входит в команду {count} раз(а).")
else:
    print(f"Студент '{student_to_check}' не входит в команду.")