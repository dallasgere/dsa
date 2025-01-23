import pytest
from src.leetcode.permutation_in_string_567 import PermutationInString


@pytest.fixture
def permutation_checker():
    return PermutationInString()


def test_solution_one_basic(permutation_checker):
    assert permutation_checker.solution_one("ab", "eidbaooo") == True
    assert permutation_checker.solution_one("ab", "eidboaoo") == False


def test_solution_one_same_length_strings(permutation_checker):
    assert permutation_checker.solution_one("abc", "bca") == True
    assert permutation_checker.solution_one("abc", "cab") == True
    assert permutation_checker.solution_one("abc", "acb") == True
    assert permutation_checker.solution_one("abc", "bac") == True
    assert permutation_checker.solution_one("abc", "cba") == True
    assert permutation_checker.solution_one("abc", "abc") == True
    assert permutation_checker.solution_one("abc", "abd") == False


def test_solution_one_no_permutation(permutation_checker):
    assert permutation_checker.solution_one("abc", "def") == False
    assert permutation_checker.solution_one("abc", "acx") == False
    assert permutation_checker.solution_one("abc", "abx") == False
    assert permutation_checker.solution_one("abc", "xbc") == False


def test_solution_one_repeated_characters(permutation_checker):
    assert permutation_checker.solution_one("aab", "eidbaaooo") == True
    assert permutation_checker.solution_one("aab", "eidboaoo") == False


def test_solution_one_edge_cases(permutation_checker):
    assert permutation_checker.solution_one("a" * 10000, "a" * 10000 + "b") == True
    assert permutation_checker.solution_one("a" * 10000, "b" + "a" * 10000) == True
    assert (
        permutation_checker.solution_one("a" * 10000, "b" + "a" * 9999 + "b") == False
    )
