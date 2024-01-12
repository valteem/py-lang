import pytest

from langpy.instance_var_pass import A, pass_instance_var, pass_plain_var

def test_pass_instance_ver():

    a = A(1, "old", [11, 21, 31])

    pass_instance_var(a, 2, "new", 41)

    assert a.num == 2                 # int class attribute "passed by reference"
    assert a.txt == "new"             # str class attribute "passed by reference"
    assert a.lst == [11, 21, 31, 41]  # list class attribute "passed by reference"

    n = 2
    t = "original"
    l = [51, 61]

    pass_plain_var(n, t, l)

    assert n == 2                     # int variable "passed by value" (refers to immutable object)
    assert t == "original"            # str variable "passed by value" (refers to immutable object)
    assert l == [51, 61, 99]          # list variable "passed by reference" (refers to mutable object)

