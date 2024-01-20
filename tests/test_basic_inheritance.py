import pytest

from langpy.basic_inheritance import B

def test_basic_inheritance():

    b = B()

    assert b.a == 1
    assert b.b == 2
    assert b.c == 3