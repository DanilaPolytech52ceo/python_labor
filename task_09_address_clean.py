raw_addresses = [
    "  г. Новосибирск, ул. Советская, д. 21 ",
    "г.Самара;ул.Молодогвардейская,д.44",
    " г. Тюмень,ул. Республики ;д. 7  ",
]

# Здесь будем собирать очищенные и приведённые к одному виду адреса
normalized_addresses = []

for raw_address in raw_addresses:
    # Убираем лишние пробелы по краям и приводим разделители к запятой
    prepared = raw_address.strip()
    prepared = prepared.replace(";", ",")
    prepared = prepared.replace(", ", ",")
    prepared = prepared.replace(" ,", ",")
    # Нормализуем пробелы после сокращений
    prepared = prepared.replace("г.", "г. ")
    prepared = prepared.replace("ул.", "ул. ")
    prepared = prepared.replace("д.", "д. ")

    # Схлопываем повторяющиеся пробелы внутри строки
    while "  " in prepared:
        prepared = prepared.replace("  ", " ")

    # Возвращаем единый формат: запятая и один пробел после неё
    prepared = prepared.replace(",", ", ")

    while "  " in prepared:
        prepared = prepared.replace("  ", " ")

    normalized_addresses.append(prepared.strip())

# Сравниваем исходные строки и результат нормализации
print("=== СРАВНЕНИЕ ===")

for number, raw_address in enumerate(raw_addresses, start=1):
    print(f"#{number}")
    print(f"ДО: '{raw_address}'")
    print(f"ПОСЛЕ: '{normalized_addresses[number - 1]}'")
    print()
