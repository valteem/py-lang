import pytest

from langpy.override import Base, Heir

def test_override():

    b = Base(1)
    h1 = Heir("apples")
    h2 = Heir(2)

    assert b.show() == 1
    assert h1.show() == "apples"
    assert h2.show() == "2"
