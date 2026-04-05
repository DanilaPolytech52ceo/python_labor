# Сведения об авторе работы
student_name = "Александров Даниил Михайлович"
group_number = "52501"

# Сведения об объекте
project_name = 'ЖК "Северная Долина", корпус 1'
floors = 27
height = 85
is_residential = True
construction_year = 2015

# Делаем тип объекта более читаемым в выводе
if residential_status:
	building_type = "Жилой"
else:
	building_type = "Нежилой"

# Выводим паспорт объекта в человекочитаемом виде
print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Составитель: {student_full_name}")
print(f"Группа: {student_group}")
print()
print(f"Объект: {building_name}")
print(f"Этажность: {floor_count} этажей")
print(f"Высота: {building_height} м")
print(f"Тип: {building_type}")
print(f"Год постройки: {year_built}")

# Дополнительные сведения об объекте:
# Расположение объекта:
# г. Санкт-Петербург, пос. Парголово, ул. Фёдора Абрамова, д. 8
# Почему выбрал:
# массовая жилая застройка, типичный пример панельного жилья нового поколения
