import ifcopenshell
import ifcopenshell.api
import ifcopenshell.util.element


IFC_FILEPATH = "model.ifc"
MIN_WIDTH = 0.8
MODIFIED_OUTPUT = "modifiedifc"
FILTERED_DOORS_OUTPUT = "doors_filtered.ifc"


# В этом варианте я просто иду по пунктам задания сверху вниз.
try:
    model = ifcopenshell.open(IFC_FILEPATH)
except Exception as error:
    print("Не получилось открыть файл:", error)
    raise SystemExit

print("===== Задание 1. Количество стен =====")
walls = model.by_type("IfcWall")
print("Количество стен:", len(walls))

print("\n===== Задание 2. Первая стена =====")
first_wall = None
if len(walls) > 0:
    first_wall = walls[0]
    print("GlobalId:", getattr(first_wall, "GlobalId", None))
    print("Name:", getattr(first_wall, "Name", None))
    print("ObjectType:", getattr(first_wall, "ObjectType", None))
    print("IFC-тип:", first_wall.is_a())
else:
    print("Стен в модели нет.")

print("\n===== Задание 3. Property Sets первой стены =====")
if first_wall is not None:
    psets = ifcopenshell.util.element.get_psets(first_wall)
    if len(psets) == 0:
        print("Свойств у стены не нашлось.")
    for pset_name, props in psets.items():
        print("Pset:", pset_name)
        for prop_name, prop_value in props.items():
            print(" ", prop_name, "=", prop_value)
else:
    print("Первой стены нет, поэтому свойства вывести нельзя.")

print("\n===== Задание 4. Этажи и схема модели =====")
storeys = model.by_type("IfcBuildingStorey")
print("IFC-схема модели:", model.schema)
print("Количество этажей:", len(storeys))
if len(storeys) == 0:
    print("Этажи не найдены.")
for s in storeys:
    print("Этаж:", getattr(s, "Name", None), "Elevation:", getattr(s, "Elevation", None))

print("\n===== Задание 5. Двери =====")
doors = model.by_type("IfcDoor")
if len(doors) == 0:
    print("Дверей в модели нет.")
for d in doors:
    print("Дверь:", getattr(d, "Name", None), "ширина:", getattr(d, "OverallWidth", None), "высота:", getattr(d, "OverallHeight", None))

print("\n===== Задание 6. Узкие двери =====")
narrow_doors = []
for d in doors:
    width = getattr(d, "OverallWidth", None)
    if width is not None:
        if width < MIN_WIDTH:
            narrow_doors.append(d)

for d in narrow_doors:
    print("Узкая дверь:", getattr(d, "Name", None), "ширина:", getattr(d, "OverallWidth", None))
print("Всего узких дверей:", len(narrow_doors))

print("\n===== Задание 7. Изменение и сохранение =====")
if first_wall is not None:
    old_name = getattr(first_wall, "Name", None)
    if old_name is None:
        old_name = "Без имени"
    first_wall.Name = "MODIFIED_" + old_name

    # Тут пробую найти или создать набор свойств для стены.
    wall_pset = None
    for rel in getattr(first_wall, "IsDefinedBy", []) or []:
        if rel.is_a("IfcRelDefinesByProperties"):
            p = getattr(rel, "RelatingPropertyDefinition", None)
            if p is not None and p.is_a("IfcPropertySet") and getattr(p, "Name", None) == "Pset_WallCommon":
                wall_pset = p
    if wall_pset is None:
        wall_pset = ifcopenshell.api.run("pset.add_pset", model, product=first_wall, name="Pset_WallCommon")
    ifcopenshell.api.run("pset.edit_pset", model, pset=wall_pset, properties={"IsExternal": True})
    print("Первая стена изменена.")
else:
    print("Менять нечего, потому что стены нет.")

model.write(MODIFIED_OUTPUT)
print("Сохранен файл:", MODIFIED_OUTPUT)

# Этот экспорт сделан упрощенно для учебного примера.
try:
    new_file = ifcopenshell.file(schema=model.schema)
    for t in ["IfcProject", "IfcSite", "IfcBuilding", "IfcBuildingStorey"]:
        for obj in model.by_type(t):
            new_file.add(obj)
    for d in narrow_doors:
        new_file.add(d)
    new_file.write(FILTERED_DOORS_OUTPUT)
except Exception as error:
    print("Не получилось сделать отдельный файл только с дверями:", error)
    print("Поэтому сохраняю просто копию модели.")
    model.write(FILTERED_DOORS_OUTPUT)

check_model = ifcopenshell.open(FILTERED_DOORS_OUTPUT)
print("Сохранен файл с дверями:", FILTERED_DOORS_OUTPUT)
print("Количество дверей после проверки:", len(check_model.by_type("IfcDoor")))
