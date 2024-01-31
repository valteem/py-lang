import pytest

from typing import TYPE_CHECKING

from langpy.selected import name_encode

def test_type_checking():
    if TYPE_CHECKING:
        assert 1 == 2
    else:
        assert 1 == 1

def test_name_encode():
    assert name_encode('0123456789abcdefgh', 8) == b"01234567"

from langpy.selected import EnumVal

def test_enum_val():
    assert EnumVal.SEL_1 == 1
    assert EnumVal.SEL_2 == 3
    assert EnumVal.SEL_3 == 2