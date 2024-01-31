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