from datetime import date
from .forecast_type import ForecastType


class Forecast:
    def __init__(self, current_temp, humidity, wind, high_temp=None, low_temp=None, description='', forecast_date=date.today(), forecast_type=ForecastType.TODAY):
        self._current_temp = current_temp
        self._humidity = humidity
        self._wind = wind
        self._high_temp = high_temp
        self._low_temp = low_temp
        self._description = description
        self._forecast_date = forecast_date
        self._forecast_type = forecast_type


    @property
    def current_temp(self):
        return self._current_temp

    @property
    def forecast_date(self):
        return self._forecast_date

    @property
    def humidity(self):
        return self._humidity

    @property
    def wind(self):
        return self._wind

    @property
    def description(self):
        return self._description

    def __str__(self):
        pass
    