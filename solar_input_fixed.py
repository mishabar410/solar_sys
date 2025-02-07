from solar_objects import CelestialBody


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if True or object_type == "star":  # FIXME: Добавь данные с файла
                star = CelestialBody(
                    "star",
                    1000,
                    1,
                    2,
                    0.03,
                    0.04,
                    0,
                    0,
                    10,
                    "red",
                    None
                )
                parse_star_parameters(line, star)
                objects.append(star)
            elif True or object_type == "planet":
                planet = CelestialBody(
                    "planet"
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    5,
                    "green",
                    None
                    )
                parse_planet_parameters(line, planet)
                objects.append(planet)
                # FIXME: Делай тоже самое для планет
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    line = line.split()
    star.R = line[1]
    star.color = line[2]
    star.m = line[3]
    star.x = line[4]
    star.y = line[5]
    star.Vx = line[6]
    star.Vy = line[7]

    pass  # FIXME: not done yet


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    line = line.split()
    planet.R = line[1]
    planet.color = line[2]
    planet.m = line[3]
    planet.x = line[4]
    planet.y = line[5]
    planet.Vx = line[6]
    planet.Vy = line[7]
    
    pass  # FIXME: not done yet...


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('type',  #!!!
                                             obj.R,
                                             obj.color,
                                             obj.m, 
                                             obj.x, 
                                             obj.y, 
                                             obj.Vx, 
                                             obj.Vy
                                             )
                  )
            # FIXME: should store real values


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
