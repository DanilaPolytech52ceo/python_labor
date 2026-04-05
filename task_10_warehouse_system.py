stock = {
    "Газоблок": {"quantity": 2200, "price": 96.00, "min_quantity": 600},
    "Клей": {"quantity": 180, "price": 410.00, "min_quantity": 70},
    "Плитка": {"quantity": 14, "price": 1450.00, "min_quantity": 20},
    "Шпаклёвка": {"quantity": 55, "price": 330.00, "min_quantity": 30},
    "Ламинат": {"quantity": 40, "price": 1750.00, "min_quantity": 25},
}

# Печатаем заголовок таблицы складского отчёта
print("=" * 70)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 70)
print()
print("Материал | Кол-во | Цена | Мин. | Стоимость")
print("-" * 70)

# Переменные для общей аналитики по складу
summary_cost = 0
low_stock_items = []
max_cost_name = ""
max_cost_value = 0

for material_name, material_data in stock.items():
    # Извлекаем значения по текущему материалу
    amount = material_data["quantity"]
    unit_price = material_data["price"]
    min_amount = material_data["min_quantity"]
    full_cost = amount * unit_price

    # Накапливаем общую стоимость остатков
    summary_cost += full_cost

    # Запоминаем материал с максимальной стоимостью остатка
    if full_cost > max_cost_value:
        max_cost_value = full_cost
        max_cost_name = material_name

    # Проверяем, не опустился ли остаток ниже минимального уровня
    warning_mark = ""
    if amount < min_amount:
        warning_mark = "  CRITICAL"
        low_stock_items.append(f"{material_name}: {amount} < {min_amount}")

    print(
        f"{material_name} | {amount} | {unit_price:.2f} | "
        f"{min_amount} | {full_cost:.2f}{warning_mark}"
    )

print("=" * 70)
print(f"ОБЩАЯ СТОИМОСТЬ: {summary_cost:.2f} руб")
print(
    f"Самый дорогой: {max_cost_name} "
    f"({max_cost_value:.2f} руб)"
)
print()
print(f"КРИТИЧЕСКИЕ ОСТАТКИ ({len(low_stock_items)}):")

# Выводим список проблемных позиций, если они есть
if low_stock_items:
    for material_name in low_stock_items:
        print(f"- {material_name}")
else:
    print("Нет критических остатков")

print()
print("=== ВЫДАЧА МАТЕРИАЛА ===")

issue_name = "Клей"
issue_amount = 35

# Проверяем наличие материала и достаточность остатка перед выдачей
if issue_name in stock:
    current_amount = stock[issue_name]["quantity"]

    if current_amount >= issue_amount:
        stock[issue_name]["quantity"] -= issue_amount
        print(f"Выдано {issue_amount} единиц: '{issue_name}'")
        print(
            f"Остаток: {current_amount} -> "
            f"{stock[issue_name]['quantity']}"
        )
    else:
        print("Недостаточно материала на складе")
else:
    print("Материал не найден")
