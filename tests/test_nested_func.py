import pytest

from langpy.nested_func import outer

def test_nested_func():
    assert outer(1, 2)(5, 6) == 21