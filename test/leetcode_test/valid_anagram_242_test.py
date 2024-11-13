import pytest
from src.leetcode.valid_anagram_242 import ValidAnagram


@pytest.fixture
def anagram_checker():
    return ValidAnagram()


def test_valid_anagram(anagram_checker):
    assert anagram_checker.isAnagram("anagram", "nagaram") == True


def test_invalid_anagram(anagram_checker):
    assert anagram_checker.isAnagram("rat", "car") == False


def test_same_word(anagram_checker):
    assert anagram_checker.isAnagram("hello", "hello") == True


def test_empty_strings(anagram_checker):
    assert anagram_checker.isAnagram("", "") == True


def test_different_lengths(anagram_checker):
    assert anagram_checker.isAnagram("ab", "abc") == False


def test_case_sensitive(anagram_checker):
    assert anagram_checker.isAnagram("Anagram", "nagaram") == False


def test_special_characters(anagram_checker):
    assert anagram_checker.isAnagram("a!b@c#", "#c@b!a") == True


def test_numbers(anagram_checker):
    assert anagram_checker.isAnagram("123", "321") == True


def test_mixed_characters(anagram_checker):
    assert anagram_checker.isAnagram("Ab1!", "1!bA") == True


def test_unicode_characters(anagram_checker):
    assert anagram_checker.isAnagram("こんにちは", "はちにんこ") == True
