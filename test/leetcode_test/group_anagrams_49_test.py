import pytest
from typing import List
from src.leetcode.group_anagrams_49 import GroupAnagrams


@pytest.fixture
def group_anagrams():
    return GroupAnagrams()


def test_empty_input(group_anagrams):
    assert group_anagrams.groupAnagrams([]) == []


def test_single_word(group_anagrams):
    assert group_anagrams.groupAnagrams(["hello"]) == [["hello"]]


def test_no_anagrams(group_anagrams):
    input_strs = ["cat", "dog", "bird"]
    expected = [["cat"], ["dog"], ["bird"]]
    assert sorted(group_anagrams.groupAnagrams(input_strs)) == sorted(expected)


def test_simple_anagrams(group_anagrams):
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert sorted(map(sorted, group_anagrams.groupAnagrams(input_strs))) == sorted(
        map(sorted, expected)
    )


def test_anagrams_with_empty_string(group_anagrams):
    input_strs = ["", "b", ""]
    expected = [["", ""], ["b"]]
    assert sorted(map(sorted, group_anagrams.groupAnagrams(input_strs))) == sorted(
        map(sorted, expected)
    )


def test_anagrams_with_different_lengths(group_anagrams):
    input_strs = ["a", "aa", "aaa", "aaaa"]
    expected = [["a"], ["aa"], ["aaa"], ["aaaa"]]
    assert sorted(group_anagrams.groupAnagrams(input_strs)) == sorted(expected)


def test_large_input(group_anagrams):
    input_strs = ["abc"] * 1000 + ["cba"] * 1000 + ["bac"] * 1000
    result = group_anagrams.groupAnagrams(input_strs)
    assert len(result) == 1
    assert len(result[0]) == 3000
    assert set(result[0]) == {"abc", "cba", "bac"}


@pytest.mark.parametrize(
    "input_strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_parameterized_inputs(group_anagrams, input_strs, expected):
    assert sorted(map(sorted, group_anagrams.groupAnagrams(input_strs))) == sorted(
        map(sorted, expected)
    )


def test_get_groups_method(group_anagrams):
    groups = {}
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    group_anagrams.get_groups(groups, strs)

    expected_groups = {"aet": [], "ant": [], "abt": []}
    assert groups == expected_groups
