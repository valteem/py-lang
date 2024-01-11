import pytest

from langpy.rbtree import RBTree, Node

def build_tree_left() -> RBTree:
    """
    Tree for testing left rotation:

            2
          /    \
         /      \
        1        4
               /   \
              /     \
             3       5

    """

    t = RBTree()

    n2 = Node(2)
    n2.parent = t.dummy
    t.root = n2

    n1 = Node(1)
    n2.left = n1
    n1.parent = n2
    n1.left = t.dummy
    n1.right = t.dummy

    n4 = Node(4)
    n4.parent = n2
    n2.right = n4

    n3 = Node(3)
    n3.parent = n4
    n4.left = n3
    n3.left = t.dummy
    n3.right = t.dummy

    n5 = Node(5)
    n5.parent = n4
    n4.right = n5
    n5.left = t.dummy
    n5.right = t.dummy

    return t

def test_rotate_left():
    """
            2                                      4
          /    \                    \            /   \
         /      \                    \          /     5
        1        4       ============ \        2
               /   \     ============ /       /  \
              /     \                /       /    \
             3       5              /       1      3
    """
    t = build_tree_left()
    t.rotate_left(t.root)

    #4
    assert t.root.key == 4
    assert t.root.parent.key == "dummy"

    #2
    assert t.root.left.key == 2
    assert t.root.left.parent.key == 4

    #1
    assert t.root.left.left.key == 1
    assert t.root.left.left.parent.key == 2
    assert t.root.left.left.left.key == "dummy"
    assert t.root.left.left.right.key == "dummy"

    #3
    assert t.root.left.right.key == 3
    assert t.root.left.right.parent.key == 2
    assert t.root.left.right.left.key == "dummy"
    assert t.root.left.right.right.key == "dummy"

    #5
    assert t.root.right.key == 5
    assert t.root.right.parent.key == 4
    assert t.root.right.left.key == "dummy"
    assert t.root.right.right.key == "dummy"    

def build_tree_right() -> RBTree:
    """
    Tree for testing right rotation:

               4    
             /   \  
            /     5 
           2        
          / \       
         /   \      
        1     3     

    """
    t = RBTree()

    n4 = Node(4)
    t.root = n4
    n4.parent = t.dummy

    n2 = Node(2)
    n2.parent = n4
    n4.left = n2

    n1 = Node(1)
    n1.parent = n2
    n2.left = n1
    n1.left = t.dummy
    n1.right = t.dummy

    n3 = Node(3)
    n3.parent = n2
    n2.right = n3
    n3.left = t.dummy
    n3.right = t.dummy

    n5 = Node(5)
    n5.parent = n4
    n4.right = n5
    n5.left = t.dummy
    n5.right = t.dummy

    return t

def test_rotate_right():
    """
              4                              2
            /   \                \         /   \
           /     5                \       /     \
          2           ============ \     1       4
         / \          ============ /            /  \
        /   \                     /            /    \
       1     3                   /            3      5   
    """
    t = build_tree_right()
    t.rotate_right(t.root)

    # 2
    assert t.root.key == 2
    assert t.root.parent.key == "dummy"

    #1
    assert t.root.left.key == 1
    assert t.root.left.parent.key == 2
    assert t.root.left.left.key == "dummy"
    assert t.root.left.right.key == "dummy"

    #4
    assert t.root.right.key == 4
    assert t.root.right.parent.key == 2

    #3
    assert t.root.right.left.key == 3
    assert t.root.right.left.parent.key == 4
    assert t.root.right.left.left.key == "dummy"
    assert t.root.right.left.right.key == "dummy"
