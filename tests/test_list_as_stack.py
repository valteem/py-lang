import pytest

def test_list_as_stack():

    s = []
    r = 5

    for i in range(r):
        s.append(i)
        assert s == [x for x in range(i + 1)]
    
    for i in range(r):
        v = s.pop()
        assert v == r - i - 1
        assert s == [x for x in range(r -i - 1)]