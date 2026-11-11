order = input("Название заказа: ")
client = input("Имя заказчика: ")

item1 = input("Название первой позиции: ")
q1 = int(input("Количество первой позиции: "))
p1 = float(input("Цена первой позиции: "))

item2 = input("Название второй позиции: ")
q2 = int(input("Количество второй позиции: "))
p2 = float(input("Цена второй позиции: "))

delivery = float(input("Стоимость доставки: "))
discount_percent = float(input("Скидка в процентах: "))
cash = float(input("Внесенная сумма: "))

cost1 = q1 * p1
cost2 = q2 * p2
goods_total = cost1 + cost2

discount_sum = goods_total * (discount_percent / 100)
goods_discounted = goods_total - discount_sum
total = goods_discounted + delivery
total_qty = q1 + q2
change = cash - total

print()
print(f"Заказ: {order}")
print(f"Заказчик: {client}")
print("-" * 40)
print(f"{item1} | {q1} | {p1:.2f} | {cost1:.2f}")
print(f"{item2} | {q2} | {p2:.2f} | {cost2:.2f}")
print("-" * 40)
print(f"Сумма товаров: {goods_total:.2f} руб.")
print(f"Скидка: {discount_sum:.2f} руб.")
print(f"Сумма со скидкой: {goods_discounted:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итого к оплате: {total:.2f} руб.")
print(f"Общее количество: {total_qty} шт.")
print(f"Внесено: {cash:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
