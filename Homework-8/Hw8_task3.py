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

def write_file(text):
    f = open('paragraphs.txt', 'a+')
    f.write(text)
    f.close()


if os.path.isfile('paragraphs.txt'):
    os.remove('paragraphs.txt')
    print("success")
else:
    print("File doesn't exists!")


fake = Faker('en')
text_out = 'Английский:  ' + fake.text(50)+'\n'
write_file(text_out)

fake = Faker('it')
text_out = 'Итальянский: ' + fake.text(50)+'\n'
write_file(text_out)

fake = Faker('de')
text_out = 'Немецкий:    ' + fake.text(50)+'\n'
write_file(text_out)

fake = Faker('es')
text_out = 'Испанский:   ' + fake.text(50)+'\n'
write_file(text_out)

fake = Faker('fr')
text_out = 'Французский: ' + fake.text(50)+'\n'
write_file(text_out)