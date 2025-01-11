import pytest
from src.data_structures.monotomic_stack import MonotomicStack


@pytest.fixture
def stack():
    return MonotomicStack()


def test_next_greater_element_values(stack):
    # Test with a simple array
    arr = [4, 5, 2, 10, 8]
    expected = [5, 10, 10, -1, -1]
    assert stack.next_greater_element_values(arr) == expected

    # Test with all equal elements
    arr = [3, 3, 3, 3]
    expected = [-1, -1, -1, -1]
    assert stack.next_greater_element_values(arr) == expected

    # Test with decreasing sequence
    arr = [5, 4, 3, 2, 1]
    expected = [-1, -1, -1, -1, -1]
    assert stack.next_greater_element_values(arr) == expected

    # Test with increasing sequence
    arr = [1, 2, 3, 4, 5]
    expected = [2, 3, 4, 5, -1]
    assert stack.next_greater_element_values(arr) == expected


def test_next_greater_element_indices(stack):
    arr = [4, 5, 2, 10, 8]
    expected = [1, 3, 3, -1, -1]
    assert stack.next_greater_element_indices(arr) == expected


def test_next_smaller_element_values(stack):
    # Test with a simple array
    arr = [4, 5, 2, 10, 8]
    expected = [2, 2, -1, 8, -1]
    assert stack.next_smaller_element_values(arr) == expected

    # Test with all equal elements
    arr = [3, 3, 3, 3]
    expected = [-1, -1, -1, -1]
    assert stack.next_smaller_element_values(arr) == expected

    # Test with increasing sequence
    arr = [1, 2, 3, 4, 5]
    expected = [-1, -1, -1, -1, -1]
    assert stack.next_smaller_element_values(arr) == expected


def test_next_smaller_element_indices(stack):
    arr = [4, 5, 2, 10, 8]
    expected = [2, 2, -1, 4, -1]
    assert stack.next_smaller_element_indices(arr) == expected


def test_previous_greater_element_values(stack):
    # Test with a simple array
    arr = [4, 5, 2, 10, 8]
    expected = [-1, -1, 5, -1, 10]
    assert stack.previous_greater_element_values(arr) == expected

    # Test with all equal elements
    arr = [3, 3, 3, 3]
    expected = [-1, -1, -1, -1]
    assert stack.previous_greater_element_values(arr) == expected

    # Test with decreasing sequence
    arr = [5, 4, 3, 2, 1]
    expected = [-1, 5, 4, 3, 2]
    assert stack.previous_greater_element_values(arr) == expected


def test_previous_greater_element_indices(stack):
    arr = [4, 5, 2, 10, 8]
    expected = [-1, -1, 1, -1, 3]
    assert stack.previous_greater_element_indices(arr) == expected


def test_previous_smaller_element_values(stack):
    # Test with a simple array
    arr = [4, 5, 2, 10, 8]
    expected = [-1, -1, -1, 2, 2]
    assert stack.previous_smaller_element_values(arr) == expected

    # Test with all equal elements
    arr = [3, 3, 3, 3]
    expected = [-1, -1, -1, -1]
    assert stack.previous_smaller_element_values(arr) == expected

    # Test with increasing sequence
    arr = [1, 2, 3, 4, 5]
    expected = [-1, 1, 2, 3, 4]
    assert stack.previous_smaller_element_values(arr) == expected


def test_previous_smaller_element_indices(stack):
    arr = [4, 5, 2, 10, 8]
    expected = [-1, -1, -1, 2, 2]
    assert stack.previous_smaller_element_indices(arr) == expected


def test_empty_array(stack):
    # Test all methods with empty array
    empty = []
    assert stack.next_greater_element_values(empty) == []
    assert stack.next_greater_element_indices(empty) == []
    assert stack.next_smaller_element_values(empty) == []
    assert stack.next_smaller_element_indices(empty) == []
    assert stack.previous_greater_element_values(empty) == []
    assert stack.previous_greater_element_indices(empty) == []
    assert stack.previous_smaller_element_values(empty) == []
    assert stack.previous_smaller_element_indices(empty) == []


def test_single_element_array(stack):
    # Test all methods with single element array
    single = [1]
    assert stack.next_greater_element_values(single) == [-1]
    assert stack.next_greater_element_indices(single) == [-1]
    assert stack.next_smaller_element_values(single) == [-1]
    assert stack.next_smaller_element_indices(single) == [-1]
    assert stack.previous_greater_element_values(single) == [-1]
    assert stack.previous_greater_element_indices(single) == [-1]
    assert stack.previous_smaller_element_values(single) == [-1]
    assert stack.previous_smaller_element_indices(single) == [-1]
