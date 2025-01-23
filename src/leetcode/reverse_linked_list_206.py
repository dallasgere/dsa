"""leetcode problem 206: Reverse Linked List

link: https://leetcode.com/problems/reverse-linked-list/description/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseLinkedList:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
