# Габариты помещения в метрах
room_length = 7.2
room_width = 3.8
room_height = 3.0

# Тариф на покраску одного квадратного метра
paint_rate = 140

# Вычисляем базовые параметры комнаты
floor_square = room_length * room_width
walls_square = 2 * (room_length + room_width) * room_height
volume_value = room_length * room_width * room_height

# Считаем итоговую стоимость окраски стен
total_paint_cost = walls_square * paint_rate

# Печатаем все рассчитанные характеристики помещения
print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Длина: {room_length} м")
print(f"Ширина: {room_width} м")
print(f"Высота: {room_height} м")
print()
print(f"Площадь пола: {floor_square:.2f} м²")
print(f"Площадь стен: {walls_square:.2f} м²")
print(f"Объём помещения: {volume_value:.2f} м³")
print(f"Стоимость покраски стен: {total_paint_cost:.2f} руб.")
