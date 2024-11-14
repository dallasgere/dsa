import pytest
from src.leetcode.product_except_self_238 import ProductExceptSelf


def test_product_except_self():
    solution = ProductExceptSelf()

    # Test case 1: Basic example
    nums1 = [1, 2, 3, 4]
    assert solution.productExceptSelf(nums1) == [24, 12, 8, 6]

    # Test case 2: Array with zeros
    nums2 = [0, 1, 2, 3]
    assert solution.productExceptSelf(nums2) == [6, 0, 0, 0]

    # Test case 3: Array with multiple zeros
    nums3 = [0, 0, 2, 3]
    assert solution.productExceptSelf(nums3) == [0, 0, 0, 0]

    # Test case 4: Array with negative numbers
    nums4 = [-1, 1, 0, -3, 3]
    assert solution.productExceptSelf(nums4) == [0, 0, 9, 0, 0]

    # Test case 5: Array with all ones
    nums5 = [1, 1, 1, 1]
    assert solution.productExceptSelf(nums5) == [1, 1, 1, 1]

    # Test case 6: Array with two elements
    nums6 = [4, 5]
    assert solution.productExceptSelf(nums6) == [5, 4]

    # Test case 7: Empty array (edge case)
    nums7 = []
    assert solution.productExceptSelf(nums7) == []


def test_product_except_self_large_array():
    solution = ProductExceptSelf()

    # Test case 8: Large array
    nums8 = list(range(1, 10001))  # Array from 1 to 10000
    result = solution.productExceptSelf(nums8)
    assert len(result) == 10000
    assert result[0] != 0  # The first element should not be zero
    assert result[-1] != 0  # The last element should not be zero
