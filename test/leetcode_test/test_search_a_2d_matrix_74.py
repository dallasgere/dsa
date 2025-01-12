import pytest
from src.leetcode.search_a_2d_matrix_74 import SearchA2DMatrix


@pytest.fixture
def search_matrix():
    return SearchA2DMatrix()


def test_searchMatrix_target_present(search_matrix):
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert search_matrix.searchMatrix(matrix, target) == True


def test_searchMatrix_target_not_present(search_matrix):
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert search_matrix.searchMatrix(matrix, target) == False


def test_searchMatrix_empty_matrix(search_matrix):
    matrix = []
    target = 0
    assert search_matrix.searchMatrix(matrix, target) == False


def test_searchMatrix_single_element_matrix(search_matrix):
    matrix = [[1]]
    target = 1
    assert search_matrix.searchMatrix(matrix, target) == True


def test_searchMatrix_target_at_beginning(search_matrix):
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 1
    assert search_matrix.searchMatrix(matrix, target) == True


def test_searchMatrix_target_at_end(search_matrix):
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 60
    assert search_matrix.searchMatrix(matrix, target) == True


def test_binary_search_target_present(search_matrix):
    arr = [1, 3, 5, 7]
    target = 5
    assert search_matrix.binary_search(arr, target) == True


def test_binary_search_target_not_present(search_matrix):
    arr = [1, 3, 5, 7]
    target = 4
    assert search_matrix.binary_search(arr, target) == False


def test_binary_search_empty_array(search_matrix):
    arr = []
    target = 1
    assert search_matrix.binary_search(arr, target) == False


def test_binary_search_single_element_array(search_matrix):
    arr = [1]
    target = 1
    assert search_matrix.binary_search(arr, target) == True
