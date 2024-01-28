import pytest

from langpy.func_partial import multiple_args, multiple_args_partial, get_partial

def test_func_partial():

    assert multiple_args_partial(1) == 4

    assert get_partial(multiple_args) == None

    assert get_partial(multiple_args_partial).__name__ == 'multiple_args'