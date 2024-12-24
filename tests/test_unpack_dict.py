import pytest

def test_unpack_dict_to_string():

    template = '%(x)d/%(y)d/%(z)d'

    output = template % {'x': 1, 'y': 2, 'z': 3}

    assert output == '1/2/3'


# https://stackoverflow.com/a/7527889
def test_unpack_dict_to_function_param():

    def add(a, b, c):
        return a + b + c

    x = { 'a': 3, 'b': 1, 'c': 2 }
    r =add(**x)

    assert r == 6 