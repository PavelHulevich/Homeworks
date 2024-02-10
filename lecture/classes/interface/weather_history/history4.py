from datetime import datetime
from pathlib import Path
from typing import Protocol, TypedDict
from json import dumps


class Weather(TypedDict):
    date: str
    city: str
    sunrise: str
    sunset: str


class WeatherStorage(Protocol):
    """Interface for any storage saving weather"""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class PlainFileWeatherStorage:
    """Store weather in plain text file"""
    def __init__(self, file: Path):
        self._file = file

    def format_weather(self, weather: Weather) -> str:
        return dumps(weather)

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = self.format_weather(weather)
        with open(self._file, "a") as f:
            f.write(f"{now}\n{formatted_weather}\n")


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Saves weather in the storage"""
    storage.save(weather)


if __name__ == '__main__':
    weather: Weather = {
        'date': '2023-03-03',
        'city': 'Minsk',
        'sunrise': '04:56:41',
        'sunset': '23:25:36',
    }
    storage = PlainFileWeatherStorage(file=Path.cwd() / 'history.txt')
    save_weather(weather=weather, storage=storage)
