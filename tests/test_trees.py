from langpy.trees import Tree

import pytest

def tree_clrs_12_2() -> Tree:

    t = Tree()
    """
    Figure 12.2 CLRS
    """
    t.insert(15)
    t.insert(18)
    t.insert(6)
    t.insert(20)
    t.insert(17)
    t.insert(7)
    t.insert(3)
    t.insert(13)
    t.insert(4)
    t.insert(2)
    t.insert(9)

    return t

def test_tree():

    t = Tree()
    t.insert(2)
    t.insert(1)
    t.insert(3)
    t.insert(3) # trying to add an existing key does not add anything
    t.insert(1)

    assert t.root.key == 2
    assert t.root.left.key == 1
    assert t.root.right.key == 3

    assert t.search(t.root, 1).key == 1
    assert t.search(t.root.left, 1).key == 1
    assert t.search(t.root.right, 1) == None
    assert t.search(t.root, 4) == None

    assert t.search_iterative(t.root, 1).key == 1
    assert t.search_iterative(t.root.left, 1).key == 1
    assert t.search_iterative(t.root.right, 1) == None
    assert t.search_iterative(t.root, 4) == None


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
    assert t.search_iterative(t.root, 1).key == 1
    assert t.search_iterative(t.root, 2).key == 2
    assert t.search_iterative(t.root, 3).key == 3
    assert t.search_iterative(t.root, 4) == None   
    

    next = t.root.left
    assert next.parent.key == 3
    assert next.right == None
    assert next.key == 2
    assert t.search(next, 3) == None
    assert t.search(next, 2).key == 2
    assert t.search(next, 1).key == 1
    assert t.search(next, 4) == None
    assert t.search_iterative(next, 3) == None
    assert t.search_iterative(next, 2).key == 2
    assert t.search_iterative(next, 1).key == 1
    assert t.search_iterative(next, 4) == None

    next = next.left
    assert next.parent.key == 2
    assert next.right == None
    assert next.left == None
    assert next.key == 1
    assert t.search(next, 3) == None
    assert t.search(next, 2) == None
    assert t.search(next, 1).key == 1
    assert t.search(next, 4) == None
    assert t.search_iterative(next, 3) == None
    assert t.search_iterative(next, 2) == None
    assert t.search_iterative(next, 1).key == 1
    assert t.search_iterative(next, 4) == None


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
    assert t.search_iterative(t.root, 1).key == 1
    assert t.search_iterative(t.root, 2).key == 2
    assert t.search_iterative(t.root, 3).key == 3
    assert t.search_iterative(t.root, 4) == None

    next = t.root.right
    assert next.parent.key ==1
    assert next.left == None
    assert next.key == 2
    assert t.search(next, 1) == None
    assert t.search(next, 2).key == 2
    assert t.search(next, 3).key == 3
    assert t.search(next, 4) == None
    assert t.search_iterative(next, 1) == None
    assert t.search_iterative(next, 2).key == 2
    assert t.search_iterative(next, 3).key == 3
    assert t.search_iterative(next, 4) == None

    next = next.right
    assert next.parent.key == 2
    assert next.left == None
    assert next.right == None
    assert next.key == 3
    assert t.search(next, 1) == None
    assert t.search(next, 2) == None
    assert t.search(next, 3).key == 3
    assert t.search(next, 4) == None
    assert t.search_iterative(next, 1) == None
    assert t.search_iterative(next, 2) == None
    assert t.search_iterative(next, 3).key == 3
    assert t.search_iterative(next, 4) == None

def test_min_max():
     
    t = Tree()
    t.insert(11)
    t.insert(7)
    t.insert(19)
    t.insert(2)
    t.insert(9)
    t.insert(8)
    t.insert(14)

    assert t.maximum(t.root).key == 19
    assert t.maximum_recursive(t.root).key == 19
    assert t.minimum(t.root).key == 2
    assert t.minimum_recursive(t.root).key == 2

    n = t.root.left
    assert t.maximum(n).key == 9
    assert t.maximum_recursive(n).key == 9
    assert t.minimum(n).key == 2
    assert t.minimum_recursive(n).key == 2

    n = t.root.left.left
    assert t.maximum(n).key == 2
    assert t.maximum_recursive(n).key == 2
    assert t.minimum(n).key == 2
    assert t.minimum_recursive(n).key == 2

    n = t.root.left.right
    assert t.maximum(n).key == 9
    assert t.maximum_recursive(n).key == 9
    assert t.minimum(n).key == 8
    assert t.minimum_recursive(n).key == 8

    n = t.root.right
    assert t.maximum(n).key == 19
    assert t.maximum_recursive(n).key == 19
    assert t.minimum(n).key == 14
    assert t.minimum_recursive(n).key == 14


def test_next_prev():

    t = tree_clrs_12_2()

    assert t.next_node(t.search_iterative(t.root, 13)).key == 15
    assert t.next_node(t.search_iterative(t.root, 9)).key == 13
    assert t.next_node(t.search_iterative(t.root, 4)).key == 6
    assert t.next_node(t.search_iterative(t.root, 17)).key == 18
    assert t.next_node(t.search_iterative(t.root, 18)).key == 20
    assert t.next_node(t.search_iterative(t.root, 20)) == None

    assert t.prev_node(t.search_iterative(t.root, 13)).key == 9
    assert t.prev_node(t.search_iterative(t.root, 9)).key == 7
    assert t.prev_node(t.search_iterative(t.root, 4)).key == 3
    assert t.prev_node(t.search_iterative(t.root, 17)).key == 15
    assert t.prev_node(t.search_iterative(t.root, 18)).key == 17
    assert t.prev_node(t.search_iterative(t.root, 2)) == None

def test_inorder_walk():

    t = tree_clrs_12_2()

    assert t.inorder_walk(t.root) == [2, 3, 4, 6, 7, 9, 13, 15, 17, 18, 20]