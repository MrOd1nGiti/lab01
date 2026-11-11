first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print(f"До обмена: первой - {first_room}, второй - {second_room}")

temp = first_room
first_room = second_room
second_room = temp

print(f"После обмена: первой - {first_room}, второй - {second_room}")
