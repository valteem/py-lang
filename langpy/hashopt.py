"""
Prep stuff for various hashing options

Loosely based on CLRS 11.3 examples
"""

def div_mod_power_of_2(input: int, mod_power_of_2: int) -> (int, int):
    return (input % (1 << mod_power_of_2), input & ((1 << mod_power_of_2) - 1)) # h(k) is just the p lowest-order bits of k