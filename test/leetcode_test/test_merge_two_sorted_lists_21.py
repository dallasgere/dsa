import pytest
from typing import List
from src.leetcode.merge_two_sorted_lists_21 import ListNode, MergeTwoSortedLists


def create_linked_list(values: List[int]) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head: ListNode) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


@pytest.fixture
def solution():
    return MergeTwoSortedLists()


def test_merge_two_sorted_lists(solution):
    # Test case 1: Both lists non-empty
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.solution(list1, list2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]

    # Test case 2: One list empty
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = solution.solution(list1, list2)
    assert linked_list_to_list(merged) == [0]

    # Test case 3: Both lists empty
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = solution.solution(list1, list2)
    assert linked_list_to_list(merged) == []

    # Test case 4: Lists of different lengths
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6, 7, 8])
    merged = solution.solution(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6, 7, 8]

    # Test case 5: One list is a subset of the other
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([1, 2, 3, 4, 5])
    merged = solution.solution(list1, list2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 3, 4, 5, 5]
