import pytest

from langpy.type_inherit import A, B

def test_type_inherit():

    a = A(1)
    b = B(1)

    assert isinstance(b, A) == True

    assert str(type(a)) == "<class 'langpy.type_inherit.A'>"
    assert str(type(b)) == "<class 'langpy.type_inherit.B'>"

    assert (a == b) == True