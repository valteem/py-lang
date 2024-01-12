"""
Passing class variable as function argument
"""

from typing import List

class A:
    def __init__(self, num: int, txt: str, lst: List[int]) -> None:
        self.num = num
        self.txt = txt
        self.lst = lst

def pass_instance_var(a: A, newnum: int, newtxt: str, new_list_elt: int) -> None:
    a.num = newnum
    a.txt = newtxt
    a.lst.append(new_list_elt)

def pass_plain_var(n: int, t: str, l: List[int]):
    n *= 2
    t = "changed"
    l.append(99)