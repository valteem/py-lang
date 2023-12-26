from langpy.trees import Tree

import pytest

def test_tree():

    t = Tree()
    t.insert(2)
    t.insert(1)
    t.insert(3)

    assert t.root.key == 2
    assert t.root.left.key == 1
    assert t.root.right.key == 3