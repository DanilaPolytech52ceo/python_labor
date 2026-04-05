# Стоимость единицы товара и число позиций
unit_price = int(input("Введите стоимость (целое число): "))
item_count = int(input("Количество товара (целое число): "))

# Находим цену заказа без учёта скидки
initial_sum = unit_price * item_count

# Подбираем подходящий процент скидки
if initial_sum < 1000:
    sale_percent = 0
elif initial_sum <= 5000:
    sale_percent = 5
else:
    sale_percent = 10

# Считаем скидку и финальную сумму
sale_value = initial_sum * sale_percent / 100
payment_sum = initial_sum - sale_value

# Выводим промежуточные и итоговые данные по заказу
print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Цена за единицу: {unit_price:.2f} руб.")
print(f"Количество товара: {item_count}")
print(f"Стоимость без скидки: {initial_sum:.2f} руб.")
print(f"Размер скидки: {sale_percent}%")
print(f"Сумма скидки: {sale_value:.2f} руб.")
print(f"Итоговая стоимость: {payment_sum:.2f} руб.")ы
