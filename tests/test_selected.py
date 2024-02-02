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

from langpy.selected import key_encode, dict_encode, value_serializer

def test_encode():
    assert key_encode(1) == '1'
    assert dict_encode({1: "old", 11: "new"}) == '{"1": "old", "11": "new"}'
    assert value_serializer(1.1E+1) == "11.0"

from langpy.selected import Product

def test_product():
    p1 = Product(1.0, 10) # 'hidden' __init__() produced by 'dataclass' decorator
    assert p1.amout() == 10.0
    assert p1.places == ['main', 'reserve', 'external']
    p2 = Product(3.2, 4)
    assert p2.amout() == 12.8
    assert p1 != p2

from langpy.selected import Encoder

def test_encoder():
    e1 = Encoder()
    e1.set_src('csv')
    e1.set_dst('xml')
    assert e1.convert("text") == "csv_to_xml text"
    e2 = Encoder()
    e2.set_src('json')
    e2.set_dst('xml')
    assert e2.convert("text") == "json_to_xml text"
    e3 = Encoder()
    e3.set_src('xml')
    e3.set_dst('csv')
    assert e3.convert("text") == "no available encode path"
    """
    Fails, 'src' and 'dst are shared among e1, e2, e3
    """
#    assert e1.convert("text") == "csv_to_xml text"