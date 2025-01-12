import pytest
from src.leetcode.koko_eating_bananas_875 import KokoEatingBananas


@pytest.fixture
def koko():
    return KokoEatingBananas()


def test_min_eating_speed_three_example1(koko):
    assert koko.min_eating_speed_three([3, 6, 7, 11], 8) == 4


def test_min_eating_speed_three_example2(koko):
    assert koko.min_eating_speed_three([30, 11, 23, 4, 20], 5) == 30


def test_min_eating_speed_three_example3(koko):
    assert koko.min_eating_speed_three([30, 11, 23, 4, 20], 6) == 23


def test_min_eating_speed_three_single_pile(koko):
    assert koko.min_eating_speed_three([10], 4) == 3


def test_min_eating_speed_three_all_same_piles(koko):
    assert koko.min_eating_speed_three([5, 5, 5, 5], 4) == 5


def test_min_eating_speed_three_large_numbers(koko):
    assert koko.min_eating_speed_three([1000000000], 2) == 500000000


def test_min_eating_speed_three_edge_case(koko):
    assert koko.min_eating_speed_three([1, 1, 1, 1], 8) == 1
