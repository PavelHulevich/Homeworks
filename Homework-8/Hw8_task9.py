"""Задание 9:
Напишите программу, которая читает текстовый файл, содержащий логи сервера, и выводит
на экран статистику по количеству и типам запросов. Программа не должна загружать весь
файл в память. Формат файла следующий: каждая строка содержит дату и время запроса, IPадрес клиента,
 метод запроса (GET, POST, PUT, DELETE и т.д.), запрашиваемый ресурс, код
ответа сервера и размер ответа в байтах, разделенные пробелами.
Статистика должна включать в себя количество успешных (2xx, 3xx) и не успешных (4xx,
5xx) обращений к ресурсу (index.html, login.php, upload.php) разделенных по типу запроса
(GET/POST/PUT).
Например:
2023-04-15 12:34:56 192.168.0.1 GET /index.html 200 1024
2023-04-15 12:35:01 192.168.0.2 POST /login.php 302 512
2023-04-15 12:35:05 192.168.0.3 PUT /upload.php 403 0       """
from faker import Faker
from random import randint, choice
import datetime
import os


def collecting_server_stat(name: str) -> list:
    infile = open(name, 'r', encoding='utf-8')
    requests_good = dict()
    requests_bad = dict()
    resources_set = set()
    for line in infile:
        line_list = line.split(' ')
        resources_set.add(line_list[4])
        requests_good[line_list[3]] = 0
        requests_bad[line_list[3]] = 0
    infile.seek(0)
    stat_out = []
    for resources_curr in resources_set:
        requests_bad1 = requests_bad.copy()
        requests_good1 = requests_good.copy()
        stat = []
        stat.append(resources_curr)
        stat.append(requests_good1)
        stat.append(requests_bad1)

        infile.seek(0)
        for line in infile:
            line_list = line.split(' ')
            if line_list[4] in resources_curr:
                if int(line_list[5]) in range(200, 399):
                    stat[1][line_list[3]] += 1
                if int(line_list[5]) in range(400, 599):
                    stat[2][line_list[3]] += 1
        stat_out.append(stat)
    print(stat_out)
    infile.close()
    return stat_out


def creating_log_file(name: str, records_qnt: int) -> None:
    TYPE_OF_REQUEST = ('/index.html', '/login.php', '/upload.php')
    fake = Faker('ru')
    # Удаляем старый файл, если он есть.
    if os.path.isfile(name):
        os.remove(name)
    outfile = open(name, 'a+', encoding="utf-8")
    for _ in range(0, records_qnt):
        record = ''
        record += f'{fake.date_time_between("-3d", "now")} '
        record += f'{fake.ipv4_private(False, "c")} '
        record += f'{fake.http_method()} '
        record += f'{choice(TYPE_OF_REQUEST)} '
        record += f'{str(randint(200, 599))} '
        record += f'{choice(["0", "512", "1024", "2048"])}\n'
        outfile.writelines(record)
        print(record)
    outfile.close()


def validate_enter_data(name: str) -> bool:
    infile = open(name, 'r', encoding="utf-8")
    for line in infile:
        line_current = line.split(' ')
        if len(line_current) != 7:
            print('Ошибка. Содержимое лог-файла не соответствует протоколу')
            infile.close()
            return False
        try:
            date_time = ' '.join(line_current[:2])
            _ = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print('Ошибка. Неверная запись о дате или времени ')
            infile.close()
            return False
        try:
            _ = int(line_current[5])
        except ValueError:
            print('Ошибка. Данные времени запроса не целое число')
            return False
    infile.close()
    return True


def printing_server_stat_from_log(file_name: str) -> None:
    validate_result = validate_enter_data(file_name)
    if not validate_result:
        print('Ошибка. Данные в лог-фале не верны')
        return

    server_stat = collecting_server_stat(file_name)
    for resurse in server_stat:
        print(f'\nК ресурсу {resurse[0]} были произведены обращения:')
        print('Успешные:   ', end='')
        for k, v in resurse[1].items():
            if v != 0:
                print(f'{k}: {v}  ', end='')
        print('\nНеуспешные:   ', end='')
        for k, v in resurse[2].items():
            if v != 0:
                print(f'{k}: {v}  ', end='')
        print()


log_file_name = 'log_file'
records_quantity = 5
# creating_log_file(log_file_name, records_quantity)
printing_server_stat_from_log(log_file_name)


