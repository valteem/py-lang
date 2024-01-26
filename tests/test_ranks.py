import pytest

from langpy.ranks import round_grades

def test_round_grades():

    test_grades = [73, 67, 38, 33]
    rounded_grades = round_grades(test_grades)
    assert rounded_grades == [75, 67, 40, 33]