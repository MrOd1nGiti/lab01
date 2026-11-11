subject1 = input("Название первого предмета: ")
count1 = int(input("Количество занятий первого предмета: "))
duration1 = int(input("Продолжительность первого занятия в минутах: "))

subject2 = input("Название второго предмета: ")
count2 = int(input("Количество занятий второго предмета: "))
duration2 = int(input("Продолжительность второго занятия в минутах: "))

available_hours = float(input("Доступное время на неделю в часах: "))

minutes1 = count1 * duration1
minutes2 = count2 * duration2
total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60

available_minutes = available_hours * 60
remaining_minutes = available_minutes - total_minutes
remaining_hours = remaining_minutes / 60

load_4_weeks = total_hours * 4

print()
print("--- УЧЕБНАЯ НАГРУЗКА ---")
print(f"Предмет 1 ({subject1}): {minutes1} минут")
print(f"Предмет 2 ({subject2}): {minutes2} минут")
print(f"Общая нагрузка: {total_minutes} минут ({total_hours:.2f} ч.)")
print(f"Остаток свободного времени: {remaining_hours:.2f} ч.")
print(f"Нагрузка за 4 недели: {load_4_weeks:.2f} ч.")
