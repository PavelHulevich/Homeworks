"""
допустим, мы хотим реализовать сохранение истории всех запросов погоды. Чтобы при каждом запуске нашей программы куда-то
сохранялись её результаты, и в будущем можно было проанализировать эту информацию.
Куда мы можем сохранить эту информацию? В плоский txt-файл. В файл JSON. В базу данных SQL. В NoSQL базу данных.
Отправить куда-то по сети в какой-то веб-сервис. Вариантов много и потенциально в будущем возможно нам захочется
заменить текущий выбранный вариант на какой-то другой. Давайте реализуем модуль history.py, который будет отвечать за
сохранение истории
"""
from typing import TypedDict


class Weather(TypedDict):
    date: str
    city: str
    sunrise: str
    sunset: str


"""
WeatherStorage — это интерфейс в терминах объектно-ориентированного программирования. Этот интерфейс описывает те 
методы, которые обязательно должны присутствовать у любого хранилища погоды. Собственно говоря, у любого хранилища 
погоды должен быть как минимум метод save, который принимает на вход погоду, которую он должен сохранить.
В интерфейсе WeatherStorage нет реализации (на то он и интерфейс), он только объявляет метод save, который должен быть 
определён в любом классе, реализующем этот интерфейс.
"""


class WeatherStorage:
    def save(self, weather: Weather) -> None:
        raise NotImplementedError

    def save2(self) -> None:
        raise NotImplementedError


class PlainFileWeatherStorage(WeatherStorage):
    pass


storage = PlainFileWeatherStorage()
try:
    """
    Чтобы показать, что метод save интерфейса не реализован, мы возбуждаем в нём исключение NotImplementedError, эта 
    ошибка говорит о том, что вызываемый метод не реализован. Таким образом, если мы создадим хранилище, отнаследованное
    от этого интерфейса, не реализуем в нём метод save и вызовем его, то у нас упадёт в рантайме исключение 
    NotImplementedError:
    """
    storage.save2()
except NotImplementedError:
    pass


"""
Функция save_weather будет вызываться более высокоуровневым управляющим кодом для сохранения погоды в хранилище. Эта 
функция принимает на вход погоду weather, которую надо сохранить, и реальный экземпляр хранилища storage, которое 
реализует интерфейс WeatherStorage.
"""


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    storage.save(weather)


if __name__ == '__main__':
    weather: Weather = {
        'date': '2023-03-03',
        'city': 'Minsk',
        'sunrise': '04:56:41',
        'sunset': '23:25:36',
    }
    storage = PlainFileWeatherStorage()
    save_weather(weather=weather, storage=storage)
