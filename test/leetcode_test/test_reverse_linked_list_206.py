import pytest
from src.leetcode.reverse_linked_list_206 import ListNode, ReverseLinkedList


def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


@pytest.fixture
def reverse_linked_list():
    return ReverseLinkedList()


def test_empty_list(reverse_linked_list):
    assert reverse_linked_list.reverseList(None) == None


def test_single_node(reverse_linked_list):
    head = ListNode(1)
    reversed_head = reverse_linked_list.reverseList(head)
    assert linked_list_to_list(reversed_head) == [1]


def test_two_nodes(reverse_linked_list):
    head = create_linked_list([1, 2])
    reversed_head = reverse_linked_list.reverseList(head)
    assert linked_list_to_list(reversed_head) == [2, 1]


def test_multiple_nodes(reverse_linked_list):
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list.reverseList(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]


def test_reversed_list(reverse_linked_list):
    head = create_linked_list([5, 4, 3, 2, 1])
    reversed_head = reverse_linked_list.reverseList(head)
    assert linked_list_to_list(reversed_head) == [1, 2, 3, 4, 5]
