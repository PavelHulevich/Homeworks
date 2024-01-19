"""
Задание 3:
Напишите программу, которая генерирует случайный текст из 5 абзацев и записывает его в
файл с именем "paragraphs.txt". Программа должна использовать модуль faker
(https://faker.readthedocs.io/) для создания абзацев на английском, итальянском, немецком,
испанском, французском языках. Для генерации каждого абзаца используйте разные
провайдеры на ваше усмотрение, каждый абзац должен быть сгенерирован на новом языке.
Программа должна использовать функцию open для открытия файла в режиме записи и метод
write для записи текста в файл. Программа должна закрывать файл после записи.
"""
from faker import Faker
import os


if os.path.isfile('paragraphs.txt'):
    os.remove('paragraphs.txt')
    print("Предыдущий файл с именем paragraphs.txt удален. Создаем новый.")
else:
    print("Файл paragraphs.txt не существует. Создаем новый")


f = open('paragraphs.txt', 'a+',  encoding="utf-8")

fake = Faker('en')
text_out = f'Английский. Имя:\n{fake.name()}\n\n'
fake = Faker('it')
text_out += f'Итальянский. Адрес:\n{fake.address()}\n\n'
fake = Faker('de')
text_out += f'Немецкий. Профессия:\n{fake.job()}\n\n'
fake = Faker('es')
text_out += f'Испанский. Место работы:  \n{fake.company()}\n\n'
fake = Faker('fr')
text_out += f'Французскийю Телефон: \n{fake.phone_number()}\n\n'

f.write(text_out)
f.close()
