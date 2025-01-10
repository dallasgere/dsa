import pytest
from src.leetcode.word_subsets_916 import WordSubsets


@pytest.fixture
def solution():
    return WordSubsets()


def test_basic_functionality(solution):
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "o"]
    assert solution.wordSubsets(words1, words2) == ["facebook", "google", "leetcode"]


def test_empty_words2(solution):
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = []
    assert solution.wordSubsets(words1, words2) == words1


def test_case_sensitivity(solution):
    words1 = ["Amazon", "APPLE", "facebook", "Google"]
    words2 = ["a"]
    assert solution.wordSubsets(words1, words2) == ["Amazon", "facebook"]


def test_large_input(solution):
    words1 = ["word"] * 10000
    words2 = ["w", "o", "r", "d"]
    assert solution.wordSubsets(words1, words2) == words1
