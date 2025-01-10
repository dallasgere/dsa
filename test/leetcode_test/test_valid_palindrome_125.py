import pytest
from src.leetcode.valid_palindrome_125 import ValidPalindrom


@pytest.fixture
def palindrome_checker():
    """Fixture to create an instance of ValidPalindrom."""
    return ValidPalindrom()


def test_empty_string(palindrome_checker):
    assert palindrome_checker.isPalindrome("") == True


def test_single_character(palindrome_checker):
    assert palindrome_checker.isPalindrome("a") == True
    assert palindrome_checker.isPalindrome("A") == True


def test_simple_palindrome(palindrome_checker):
    assert palindrome_checker.isPalindrome("racecar") == True
    assert palindrome_checker.isPalindrome("RaceCar") == True


def test_non_palindrome(palindrome_checker):
    assert palindrome_checker.isPalindrome("hello") == False
    assert palindrome_checker.isPalindrome("world") == False


def test_palindrome_with_spaces_and_punctuation(palindrome_checker):
    assert palindrome_checker.isPalindrome("A man, a plan, a canal: Panama") == True
    assert palindrome_checker.isPalindrome("No 'x' in Nixon") == True


def test_non_palindrome_with_spaces_and_punctuation(palindrome_checker):
    assert palindrome_checker.isPalindrome("This is not a palindrome!") == False
