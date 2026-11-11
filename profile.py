surname = input("Введите фамилию: ")
name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст: "))
favorite_subject = input("Введите любимый предмет: ")
study_hours = float(input("Введите часы подготовки в неделю: "))

age_in_4_years = age + 4
study_hours_4_weeks = study_hours * 4
study_hours_per_day = study_hours / 7

print()
print("--- КАРТОЧКА СТУДЕНТА ---")
print(f"ФИО: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст через 4 года: {age_in_4_years}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Время подготовки за 4 недели: {study_hours_4_weeks:.2f} ч.")
print(f"Среднее время подготовки в день: {study_hours_per_day:.2f} ч.")
