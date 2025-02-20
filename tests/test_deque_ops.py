import pytest

from collections import deque

def test_basic():

    d = deque([1, 2, 3, 4, 5])

    """
    negative offset - moving items left
    """
    d.rotate(-2)
    assert [*d] == [3, 4, 5, 1, 2] #/ [*d] - unpack deque to list
    """
    positive offset - moving items right
    """
    d.rotate(4)
    assert [*d] == [4, 5, 1, 2, 3]

    d.extendleft([11, 12])
    """extendleft() adds items from a list one by one, left to right, thus order of new items in resulting deque is reversed"""
    assert [*d] == [12, 11, 4, 5, 1, 2, 3]

    d.extend([21, 22])
    assert [*d] == [12, 11, 4, 5, 1, 2, 3, 21, 22]

def test_pop():

    q = deque(['a', 'b', 'c'])

    q.append('x')

    q.pop() == 'x'
    assert q.popleft() == 'a'