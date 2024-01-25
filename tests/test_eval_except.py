import pytest

from langpy.eval_except import A
from langpy.eval_except import is_a
from langpy.eval_except import is_some_fancy_object


def test_eval_except():

    a = A()

    assert is_a(a) == True
    assert is_some_fancy_object(a) == False