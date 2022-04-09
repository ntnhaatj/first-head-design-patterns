from abc import ABC, abstractmethod
from typing import Sequence, Any
from .models import WeatherData, WeatherStatistic
from .interfaces import IDisplay, Observer, Subject
from .subject_impl import data_store


class DisplayObserverBase(IDisplay, Observer, ABC):
    @classmethod
    @abstractmethod
    def transform_to_displayed_data(cls, data: WeatherData) -> Any:
        pass

    def update(self, data: WeatherData):
        self.display(self.transform_to_displayed_data(data))


class CurrentStatsDisplay(DisplayObserverBase):
    def __init__(self, subject: Subject):
        Observer.__init__(self, subject)

    @classmethod
    def display(cls, data: str):
        print(f"[CurrentStatsDisplay] {data}")

    @classmethod
    def transform_to_displayed_data(cls, data: WeatherData) -> Any:
        return str(data)


class StatisticDisplay(DisplayObserverBase):
    @classmethod
    def display(cls, *args, **kwargs):
        for stats in cls.transform_to_displayed_data(None):
            print("[StatisticDisplay] {name} min/max/avg: {min}/{max}/{avg}".format(
                name=stats.type,
                avg=stats.avg,
                min=stats.min,
                max=stats.max,
            ))

    @classmethod
    def get_statistic(cls, data: Sequence[Any], typ3: str) -> WeatherStatistic:
        return WeatherStatistic(type=typ3,
                                min=min(data),
                                max=max(data),
                                avg=(sum(data) / len(data)))

    @classmethod
    def transform_to_displayed_data(cls, _) -> Any:
        return (
            cls.get_statistic(
                data=tuple(map(lambda x: x.temperature, data_store)),
                typ3='Temperature'),
            cls.get_statistic(
                data=tuple(map(lambda x: x.humidity, data_store)),
                typ3='Humidity'))


class ForecastDisplay(DisplayObserverBase):
    @classmethod
    def display(cls, forecast_data):
        print(f"[ForecastDisplay] {forecast_data}")

    @classmethod
    def transform_to_displayed_data(cls, data: WeatherData) -> Any:
        if data.temperature > 30:
            return "hot"
        elif data.temperature > 20:
            return "cold"
        else:
            return "very cold"
