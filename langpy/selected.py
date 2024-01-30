"""
An assortment of utility functions from across various repositories
"""

def name_encode(name:str, pos: int) -> bytes:
    return name.encode('ascii', errors='replace')[:pos]