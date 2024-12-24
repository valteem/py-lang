import pytest

def unpack_dict_to_string(template: str, input: dict ) -> str:
    return template % input

@pytest.mark.parametrize("template, input, output",
                         [('%(x)d/%(y)d/%(z)d', {'x': 1, 'y': 2, 'z': 3}, '1/2/3'),
                          ('%(z)d/%(x)d/%(y)d', {'x': 1, 'y': 2, 'z': 3}, '3/1/2')])
def test_unpack_dict_to_string(template, input, output):

    assert unpack_dict_to_string(template, input) == output


# https://stackoverflow.com/a/7527889
def test_unpack_dict_to_function_param():

    def add(a, b, c):
        return a + b + c

    x = { 'a': 3, 'b': 1, 'c': 2 }
    r =add(**x)

    assert r == 6 