from dataclasses import dataclass


@dataclass
class WeatherData:
    temperature: float
    humidity: float


@dataclass
class WeatherStatistic:
    type: str
    min: float
    max: float
    avg: float
