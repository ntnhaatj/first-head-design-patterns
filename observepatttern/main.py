from observepatttern.observer_impl import *
from observepatttern.observable_impl import *

if __name__ == "__main__":
    data_publisher = WeatherStation()

    current_stats = CurrentStatsDisplay(data_publisher)
    statistic = StatisticDisplay(data_publisher)
    forecast = ForecastDisplay(data_publisher)

    data_publisher.set_weather_stats(10, 10)
    data_publisher.set_weather_stats(10, 13)
    data_publisher.set_weather_stats(20, 15)
