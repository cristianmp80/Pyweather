from enum import Enum, unique


@unique
class ForecastType(Enum):
    TODAY='today'
    SEVENDAYS='7day'
    WEEKEND='weekend'

