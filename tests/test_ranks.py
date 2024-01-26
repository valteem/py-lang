import pytest

from langpy.ranks import round_grades
from langpy.ranks import str_to_list_of_int
from langpy.ranks import int_to_bytes

def test_round_grades():

    test_grades = [73, 67, 38, 33]
    rounded_grades = round_grades(test_grades)
    assert rounded_grades == [75, 67, 40, 33]

def test_str_to_list_of_int():
    assert str_to_list_of_int("11 21 31 41\n") == [11, 21, 31, 41]
    assert str_to_list_of_int("11 21 31 41 a\n") == []

def test_int_to_bytes():
    
    assert int_to_bytes(258, 'big') == b'\x01\x02'
    assert int_to_bytes(258, 'little') == b'\x02\x01'