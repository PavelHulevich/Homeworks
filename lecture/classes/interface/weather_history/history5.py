import json
from datetime import datetime
from pathlib import Path
from json import dumps
from typing import Protocol, TypedDict


class Weather(TypedDict):
    date: str
    city: str
    sunrise: str
    sunset: str


class HistoryRecord(TypedDict):
    date: str
    weather: str


class WeatherStorage(Protocol):
    """Interface for any storage saving weather"""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class JSONFileWeatherStorage:
    """Store weather in JSON file"""

    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile
        self._init_storage()

    def format_weather(self, weather: Weather) -> str:
        return json.dumps(weather)

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append({
            "date": str(datetime.now()),
            "weather": self.format_weather(weather)
        })
        self._write(history)

    def _init_storage(self) -> None:
        if not self._jsonfile.exists():
            self._jsonfile.write_text("[]")

    def _read_history(self) -> list[HistoryRecord]:
        with open(self._jsonfile, "r") as f:
            return json.load(f)

    def _write(self, history: list[HistoryRecord]) -> None:
        with open(self._jsonfile, "w") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)


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
    #storage = PlainFileWeatherStorage(file=Path.cwd() / 'history.txt')
    storage = JSONFileWeatherStorage(jsonfile=Path.cwd() / 'history.json.txt')
    save_weather(weather=weather, storage=storage)
