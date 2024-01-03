import pytest

from langpy.radix_tree import RadixTree

def test_radix_tree():

    r = RadixTree()

    r.insert("abc", 1)
    r.insert("ab", 2)
    r.insert("abcklm", 3)
    r.insert("abck", 4)

    assert r.root.key == ""