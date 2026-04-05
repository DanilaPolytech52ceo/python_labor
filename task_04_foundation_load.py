# Порядковый номер дня недели
weekday_number = 6

# Сопоставляем номер дня недели с его названием
if weekday_number == 1:
    weekday_name = "Понедельник"
elif weekday_number == 2:
    weekday_name = "Вторник"
elif weekday_number == 3:
    weekday_name = "Среда"
elif weekday_number == 4:
    weekday_name = "Четверг"
elif weekday_number == 5:
    weekday_name = "Пятница"
elif weekday_number == 6:
    weekday_name = "Суббота"
elif weekday_number == 7:
    weekday_name = "Воскресенье"
else:
    weekday_name = "Некорректный номер дня"

# Запрашиваем номер дня у пользователя для дальнейшего анализа
weekday_number = int(input("Введите номер дня"))

# Для выбранного номера задаём статус дня
if 1 <= weekday_number <= 5:
    day_status = "Рабочий день"
    mode_text = "8:00 - начало смены"
elif weekday_number == 6 or weekday_number == 7:
    day_status = "Выходной"
    mode_text = "Отдых"
else:
    day_status = "Не определён"
    mode_text = "Проверьте номер дня"

# Выводим сведения о выбранном дне
print("=== РАБОЧИЙ ГРАФИК ===")
print(f"Номер дня: {weekday_number}")
print(f"День недели: {weekday_name}")
print(f"Статус: {day_status}")
print(f"Режим: {mode_text}")
