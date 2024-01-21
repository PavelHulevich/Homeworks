"""
Задание 8:
Напишите программу, которая читает текстовый файл, содержащий данные о погоде в разных
городах, и выводит на экран название города с самой высокой и самой низкой температурой.
Программа не должна загружать весь файл в память. Формат файла следующий: каждая
строка содержит название города, температуру в градусах Цельсия, влажность в процентах,
давление в миллибарах, скорость ветра в метрах в секунду и осадки в миллиметрах,
разделенные запятыми. Например:
Москва,15,45,1013,3,0
Париж,18,60,1015,5,2
Нью-Йорк,20,70,1012,7,5
"""
from faker import Faker
from random import randint
import os


def creating_weather_file(city_quantity: int, name_file: str) -> None:
    # Удаляем старый файл, если он есть.
    if os.path.isfile(name_file):
        os.remove(name_file)
    # Создаем файл, в каждой строчке которого генерируется информация о погоде в городе.
    city_weather = []
    fake = Faker('ru')
    outfile = open(name_file, 'a+', encoding="utf-8")
    for _ in range(0, city_quantity):
        city_weather.clear()
        city_weather.append(fake.city())
        city_weather.append(str(randint(-15, 35)))
        city_weather.append(str(randint(15, 95)))
        city_weather.append(str(randint(900, 1100)))
        city_weather.append(str(randint(0, 35)))
        city_weather.append(str(randint(0, 15)))
        city_weather_str = ', '.join(city_weather) + '\n'
        outfile.writelines(city_weather_str)
    outfile.close()


def finding_min_max_temp(name_file: str) -> list:
    print(f'\nВ файле {name_file} содержатся следующие погодные данные по городам: ')
    infile = open(name_file, 'r', encoding="utf-8")
    city_min_t = city_max_t = infile.readline().split(', ')
    infile.seek(0)
    for line in infile:
        city_current = line.split(', ')
        print(line, end='')
        if int(city_current[1]) < int(city_min_t[1]):
            city_min_t = city_current
        if int(city_current[1]) > int(city_max_t[1]):
            city_max_t = city_current
    infile.close()
    print()
    return [city_min_t[:2], city_max_t[:2]]


def validate_enter_data(name_file: str) -> bool:
    infile = open(name_file, 'r', encoding="utf-8")
    for line in infile:
        line_current = line.split(', ')
        if len(line_current) != 6:
            print('Ошибка. Содержимое списка городов с погодными данными не соответствует протоколу')
            infile.close()
            return False
        try:
            for item in line_current[1:]:
                _ = int(item)
        except ValueError:
            print('Ошибка. Содержимое погодных данных - не целое число ')
            infile.close()
            return False
        infile.close()
        return True


def finding_min_max_temp_entry(name_file):
    validate_result = validate_enter_data(name_file)
    if not validate_result:
        print(f'Данные в файле {name_file} не соответствуют протоколу')
    else:
        min_max_cities = finding_min_max_temp(name_file)
        print(f'Минимальная температура в: {min_max_cities[0][0]}, составляет: {min_max_cities[0][1]} градусов')
        print(f'Максимальная температура в: {min_max_cities[1][0]}, составляет: {min_max_cities[1][1]} градусов')


city_qnt = 10  # Количество генерируемых городов.
name = 'weather.txt'  # Имя создаваемого файла.
creating_weather_file(city_qnt, name)
finding_min_max_temp_entry(name)
