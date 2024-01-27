import pytest

from langpy.mutable_argument import A, function_with_mutable_arg

def test_mutable_argument():

    y = 2
    for i in range(10):
        assert function_with_mutable_arg() == y
        y *= 2