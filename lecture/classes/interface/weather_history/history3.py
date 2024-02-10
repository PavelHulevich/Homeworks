"""
вариант с использованием протоколов
"""
from typing import Protocol
from typing import TypedDict


class Weather(TypedDict):
    date: str
    city: str
    sunrise: str
    sunset: str


class WeatherStorage(Protocol):
    def save(self, weather: Weather) -> None:
        pass


class PlainFileWeatherStorage:
    def save(self, weather: Weather) -> None:
        print("реализация сохранения погоды...")


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
