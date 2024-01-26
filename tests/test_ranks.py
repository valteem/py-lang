import pytest

from langpy.ranks import round_grades
from langpy.ranks import convert_str_to_list_of_int

def test_round_grades():

    test_grades = [73, 67, 38, 33]
    rounded_grades = round_grades(test_grades)
    assert rounded_grades == [75, 67, 40, 33]

def test_str_to_list_of_int():
    assert convert_str_to_list_of_int("11 21 31 41\n") == [11, 21, 31, 41]
    assert convert_str_to_list_of_int("11 21 31 41 a\n") == []