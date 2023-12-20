from langpy.hashopt import div_mod_power_of_2

import pytest

def test_div_mod_power_of_2():

    num = 77

    p = 4

    v = div_mod_power_of_2(num, p)
    assert v[0] == v[1] # h(k) is just the p lowest-order bits of k