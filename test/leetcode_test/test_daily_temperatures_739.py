import pytest
from src.leetcode.daily_temperatures_739 import DailyTemperatures


@pytest.fixture
def daily_temps():
    return DailyTemperatures()


def test_daily_temperatures_example1(daily_temps):
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temps.dailyTemperatures(temperatures) == expected


def test_daily_temperatures_example2(daily_temps):
    temperatures = [30, 40, 50, 60]
    expected = [1, 1, 1, 0]
    assert daily_temps.dailyTemperatures(temperatures) == expected


def test_daily_temperatures_example3(daily_temps):
    temperatures = [30, 60, 90]
    expected = [1, 1, 0]
    assert daily_temps.dailyTemperatures(temperatures) == expected


def test_daily_temperatures_single_element(daily_temps):
    temperatures = [30]
    expected = [0]
    assert daily_temps.dailyTemperatures(temperatures) == expected


def test_daily_temperatures_decreasing(daily_temps):
    temperatures = [90, 80, 70, 60, 50]
    expected = [0, 0, 0, 0, 0]
    assert daily_temps.dailyTemperatures(temperatures) == expected


def test_daily_temperatures_increasing(daily_temps):
    temperatures = [30, 40, 50, 60, 70]
    expected = [1, 1, 1, 1, 0]
    assert daily_temps.dailyTemperatures(temperatures) == expected


def test_daily_temperatures_same_temperature(daily_temps):
    temperatures = [70, 70, 70, 70]
    expected = [0, 0, 0, 0]
    assert daily_temps.dailyTemperatures(temperatures) == expected
