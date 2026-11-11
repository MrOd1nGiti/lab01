print("--- Фрагмент А ---")
first_a = "2"
second_a = "3"
print(f"Тип до: {type(first_a)}, значение: {first_a + second_a}")
result_a = int(first_a) + int(second_a)
print(f"Тип после: {type(result_a)}, результат суммы: {result_a}")

print()
print("--- Фрагмент Б ---")
age_str = "17"
print(f"Тип до преобразования: {type(age_str)}")
age_int = int(age_str)
age_future = age_int + 1
print(f"Тип после: {type(age_int)}, возраст через год: {age_future}")

print()
print("--- Фрагмент В ---")
first_v = 4
second_v = 7
third_v = 10
average = (first_v + second_v + third_v) / 3
print(f"Среднее арифметическое: {average}")
