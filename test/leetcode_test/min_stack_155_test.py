import pytest
from src.leetcode.min_stack_155 import MinStack


def test_min_stack_push_and_top():
    stack = MinStack()
    stack.push(5)
    assert stack.top() == 5
    stack.push(3)
    assert stack.top() == 3
    stack.push(7)
    assert stack.top() == 7


def test_min_stack_pop():
    stack = MinStack()
    stack.push(5)
    stack.push(3)
    stack.push(7)
    stack.pop()
    assert stack.top() == 3
    stack.pop()
    assert stack.top() == 5


def test_min_stack_get_min():
    stack = MinStack()
    stack.push(5)
    assert stack.getMin() == 5
    stack.push(3)
    assert stack.getMin() == 3
    stack.push(7)
    assert stack.getMin() == 3
    stack.pop()
    assert stack.getMin() == 3
    stack.pop()
    assert stack.getMin() == 5


def test_min_stack_empty():
    stack = MinStack()
    with pytest.raises(IndexError):
        stack.top()
    with pytest.raises(IndexError):
        stack.getMin()
    with pytest.raises(IndexError):
        stack.pop()


def test_min_stack_same_values():
    stack = MinStack()
    stack.push(5)
    stack.push(5)
    stack.push(5)
    assert stack.getMin() == 5
    stack.pop()
    assert stack.getMin() == 5
    stack.pop()
    assert stack.getMin() == 5


def test_min_stack_decreasing_values():
    stack = MinStack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    assert stack.getMin() == 1
    stack.pop()
    assert stack.getMin() == 2
    stack.pop()
    assert stack.getMin() == 3


def test_min_stack_increasing_values():
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    assert stack.getMin() == 1
    stack.pop()
    assert stack.getMin() == 1
    stack.pop()
    assert stack.getMin() == 1
