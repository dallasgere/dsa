import pytest
from src.leetcode.best_time_to_buy_and_sell_stock_121 import BestTimeToBuyAndSellStock


@pytest.fixture
def stock_solver():
    return BestTimeToBuyAndSellStock()


def test_profit_increasing_prices(stock_solver):
    prices = [1, 2, 3, 4, 5]
    assert stock_solver.solution(prices) == 4


def test_profit_decreasing_prices(stock_solver):
    prices = [5, 4, 3, 2, 1]
    assert stock_solver.solution(prices) == 0


def test_profit_fluctuating_prices(stock_solver):
    prices = [7, 1, 5, 3, 6, 4]
    assert stock_solver.solution(prices) == 5


def test_single_day(stock_solver):
    prices = [10]
    assert stock_solver.solution(prices) == 0

def test_identical_prices(stock_solver):
    prices = [3, 3, 3]
    assert stock_solver.solution(prices) == 0
