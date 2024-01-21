"""
Задание 7:
Напишите программу, которая создает pickle-файл, содержащий список объектов класса
Animal, определенного вами. Класс Animal должен иметь атрибуты name, species и sound и
метод make_sound, который выводит на экран звук животного. Программа должна также
загрузить pickle-файл и вызвать метод make_sound для каждого объекта в списке.
class Animal:
 def __init__(self, name, species, sound):
 …
 def make_sound(self):
 …
animals = [
 Animal("Барсик", "кот", "мяу"),
 Animal("Шарик", "собака", "гав"),
 Animal("Зорька", "лошадь", "иго-го"),
 Animal("Рыжик", "лиса", "тыф-тыф"),
 Animal("Серый", "волк", "аууу")
"""
import os
import pickle


class Animal:
    def __init__(self, name: str, species: str, sound: str):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f'{self.name} это {self.species} он делает: {self.sound}!')


def writing_pickle(animals_out: list) -> str:
    # Запись списка в pickle-файл и выдача на выход имени файла.
    if os.path.isfile('animals.pkl'):
        os.remove('animals.pkl')
    # Сериализация и запись списка в файл.
    with open('animals.pkl', 'wb') as outfile:
        pickle.dump(animals_out, outfile)
    return 'animals.pkl'


def reading_pickle(name: str) -> (list, Animal):
    with open(name, 'rb') as infile:
        animals_in = pickle.load(infile)
        return animals_in


animals = [Animal("Барсик", "кот", "мяу"), Animal("Шарик", "собака", "гав"),
           Animal("Зорька", "лошадь", "иго-го"), Animal("Рыжик", "лиса", "тыф-тыф"),
           Animal("Серый", "волк", "аууу")]

pickle_name = writing_pickle(animals)  # Сериализация списка объектов класса Анимал в пикл-файл.
animals_2 = reading_pickle(pickle_name)  # Десериализация списка из файла.
for animal in animals_2:
    animal.make_sound()
