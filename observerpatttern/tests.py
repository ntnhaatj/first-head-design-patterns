import unittest
from unittest.mock import patch, Mock

from observerpatttern.observer_impl import *
from observerpatttern.observable_impl import *


class ObserverPatternTestCase(unittest.TestCase):

    @patch('observerpatttern.observer_impl.DisplayObserverBase.update', side_effect=Mock())
    def test_all_observer_should_be_updated_when_the_weather_change(
            self, observer_update_mock):
        data_publisher = WeatherStation()

        CurrentStatsDisplay(data_publisher)
        StatisticDisplay(data_publisher)
        ForecastDisplay(data_publisher)

        data_publisher.set_weather_stats(10, 10)
        self.assertEqual(observer_update_mock.call_count, 3)

    @patch('observerpatttern.observer_impl.CurrentStatsDisplay.display', side_effect=Mock())
    @patch('observerpatttern.observer_impl.StatisticDisplay.display', side_effect=Mock())
    @patch('observerpatttern.observer_impl.ForecastDisplay.display', side_effect=Mock())
    def test_update_display_when_the_weather_change(
            self, forecast_display_mock, statistic_display_mock, current_stats_display_mock):
        data_publisher = WeatherStation()

        CurrentStatsDisplay(data_publisher)
        StatisticDisplay(data_publisher)
        ForecastDisplay(data_publisher)

        data_publisher.set_weather_stats(10, 10)
        self.assertEqual(current_stats_display_mock.call_count, 1)
        self.assertEqual(statistic_display_mock.call_count, 1)
        self.assertEqual(forecast_display_mock.call_count, 1)


if __name__ == '__main__':
    unittest.main()
