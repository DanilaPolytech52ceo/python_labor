# Начальный словарь материалов и их цен
price_map = {
    "Газоблок": 95.0,
    "Штукатурка": 360.0,
    "Клей": 420.0,
    "Плитка": 1350.0,
    "Грунтовка": 540.0,
}

print("=== ПРАЙС-ЛИСТ МАТЕРИАЛОВ ===")
print(f"Исходный словарь: {price_map}")

# Расширяем прайс двумя новыми позициями
price_map["Шпаклёвка"] = 310.0
price_map["Ламинат"] = 1800.0

print()
print("После добавления двух материалов:")
print(price_map)

# Корректируем цену клея на 10%
price_map["Клей"] = price_map["Клей"] * 1.10

# Форматируем цены как строки с двумя знаками после запятой
pretty_prices = {name: f"{price:.2f}" for name, price in price_map.items()}

print()
print("После изменения цены клея на 10%:")
print(pretty_prices)

# Удаляем одну позицию из прайса
removed_cost = price_map.pop("Грунтовка")
pretty_prices = {name: f"{price:.2f}" for name, price in price_map.items()}

print()
print(f"Удалённый материал: Грунтовка ({removed_cost:.2f} руб.)")
print(f"Итоговый словарь: {pretty_prices}")

# Находим среднюю стоимость материалов
avg_price = sum(price_map.values()) / len(price_map)

# Выводим усреднённую цену по всем оставшимся материалам
print(f"Средняя цена материалов: {avg_price:.2f} руб.")
