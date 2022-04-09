from typing import List, Any
from .models import WeatherData
from .interfaces import Subject


data_store: List[WeatherData] = list()


class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self.latest_data: WeatherData = None

    def get_data_to_notify(self) -> Any:
        return self.latest_data

    @classmethod
    def save(cls, data):
        data_store.append(data)

    def set_weather_stats(self, temperature, humidity):
        self.latest_data = WeatherData(temperature=temperature, humidity=humidity)
        self.save(self.latest_data)
        self.notify_all_observers()
