"""
An assortment of utility functions from across various repositories
"""

def name_encode(name:str, pos: int) -> bytes:
    return name.encode('ascii', errors='replace')[:pos]

from enum import IntEnum

"""
New in 3.11:
@verify(UNIQUE)
"""
class EnumVal(IntEnum):
    SEL_1 = 1
    SEL_2 = 3
    SEL_3 = 2

SEL_1 = EnumVal.SEL_1
SEL_2 = EnumVal.SEL_2
SEL_3 = EnumVal.SEL_3


import json

def key_encode(key: int) -> str:
    return json.dumps(key)

from typing import Dict

def dict_encode(dict: Dict[int, str]):
    return json.dumps(dict)

def value_serializer(value: float) -> str:
    return json.dumps(value)


from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    price: float
    qty: int
    places: List[str] = field(default_factory=lambda: ['main', 'reserve', 'external'])

    def amout(self) -> float:
        return self.price * float(self.qty)
    

class Encoder:
    src: str
    dst: str
    @classmethod
    def set_src(cls, src: str) -> None:
        cls.src = src
    @classmethod
    def set_dst(cls, dst: str) -> None:
        cls.dst = dst
    def convert(self, inp: str) -> str:
        pair = self.src + "_" + self.dst
        match pair:
            case "csv_xml":
                return "csv_to_xml" + " " + inp
            case "csv_json":
                return "csv_to_json" + " " + inp
            case "json_xml":
                return "json_to_xml" + " " + inp
            case _:
                return "no available encode path"