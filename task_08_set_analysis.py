# Списки материалов для трёх поставщиков
supplier_1 = ["Газоблок", "Клей", "Плитка", "Грунтовка"]
supplier_2 = ["Клей", "Шпаклёвка", "Грунтовка", "Ламинат"]
supplier_3 = ["Клей", "Грунтовка", "Краска", "Газоблок"]

# Переводим списки в множества
materials_1 = set(supplier_1)
materials_2 = set(supplier_2)
materials_3 = set(supplier_3)

# Получаем результаты операций над множествами
unique_materials = materials_1 | materials_2 | materials_3
shared_by_all = materials_1 & materials_2 & materials_3
only_supplier_1 = materials_1 - materials_2 - materials_3
# Находим материалы, которые встречаются ровно у двух поставщиков
shared_by_two = (materials_1 & materials_2) | (materials_1 & materials_3) | (materials_2 & materials_3)
shared_by_two = shared_by_two - shared_by_all

# Выводим результаты сравнения списков поставщиков
print("=== АНАЛИЗ ЗАКАЗОВ ===")
print(f"Материалы первого подрядчика: {supplier_1}")
print(f"Материалы второго подрядчика: {supplier_2}")
print(f"Материалы третьего подрядчика: {supplier_3}")
print()
print(f"Все уникальные материалы: {sorted(unique_materials)}")
print(f"Общие для всех: {sorted(shared_by_all)}")
print(f"Только у первого подрядчика: {sorted(only_supplier_1)}")
print(f"Ровно у двух подрядчиков: {sorted(shared_by_two)}")
