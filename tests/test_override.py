import pytest

from langpy.override import Base, Heir

def test_override():

    b = Base()
    h = Heir(2, "Heir")

    assert b.show() == (1, "Base")
    assert h.show() == "2 Heir"

    assert b.add() == 5
    assert h.add() == 6
