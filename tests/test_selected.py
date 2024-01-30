import pytest

from langpy.selected import name_encode

def test_name_encode():
    assert name_encode('0123456789abcdefgh', 8) == b"01234567"