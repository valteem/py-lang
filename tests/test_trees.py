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

    assert t.search(t.root, 1).key == 1
    assert t.search(t.root.left, 1).key == 1
    assert t.search(t.root.right, 1) == None
    assert t.search(t.root, 4) == None

def test_bst_left():
    
    t = Tree()
    t.insert(3)
    t.insert(2)
    t.insert(1)

    assert t.root.parent == None
    assert t.root.right == None
    assert t.root.key == 3
    assert t.search(t.root, 1).key == 1
    assert t.search(t.root, 2).key == 2
    assert t.search(t.root, 3).key == 3
    assert t.search(t.root, 4) == None

    next = t.root.left
    assert next.parent.key == 3
    assert next.right == None
    assert next.key == 2
    assert t.search(next, 3) == None
    assert t.search(next, 2).key == 2
    assert t.search(next, 1).key == 1
    assert t.search(next, 4) == None

    next = next.left
    assert next.parent.key == 2
    assert next.right == None
    assert next.left == None
    assert next.key == 1
    assert t.search(next, 3) == None
    assert t.search(next, 2) == None
    assert t.search(next, 1).key == 1
    assert t.search(next, 4) == None


def test_bst_right():
    
    t = Tree()
    t.insert(1)
    t.insert(2)
    t.insert(3)

    assert t.root.parent == None
    assert t.root.left == None
    assert t.root.key == 1
    assert t.search(t.root, 1).key == 1
    assert t.search(t.root, 2).key == 2
    assert t.search(t.root, 3).key == 3
    assert t.search(t.root, 4) == None

    next = t.root.right
    assert next.parent.key ==1
    assert next.left == None
    assert next.key == 2
    assert t.search(next, 1) == None
    assert t.search(next, 2).key == 2
    assert t.search(next, 3).key == 3
    assert t.search(next, 4) == None

    next = next.right
    assert next.parent.key == 2
    assert next.left == None
    assert next.right == None
    assert next.key == 3
    assert t.search(next, 1) == None
    assert t.search(next, 2) == None
    assert t.search(next, 3).key == 3
    assert t.search(next, 4) == None