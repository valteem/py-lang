import pytest

from langpy.rbtree import RBTree, Node

def test_node_reassign():
    
    np = Node(1, "v1")
    nc = Node(2, "v2")
    nc.parent = np
    np.left = nc
    nc = nc.parent

    assert nc.value == "v1"
    assert nc.left.value == "v2"
    """
    Left child still exists, but can now be referred to as 'np.left' only, not 'nc' anymore 
    """
    assert np.left.value == "v2"
    assert np.left.key == 2

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

def test_insert():
    
    t = RBTree()

    t.insert(10)

    assert t.root.red == False
    assert id(t.root.parent) == id(t.root.left) and id(t.root.parent) == id(t.root.right) # parent, left and right refer to the same "dummy" element

    t.insert(5)
    t.insert(15)
    assert t.root.left.red == True
    assert t.root.right.red == True

    t.insert(16)

    assert t.root.left.red == False
    assert t.root.right.red == False
    assert t.root.right.right.red == True # when (16) is inserted both (5) and (15) are recolored as black

    t.insert(17)

    assert t.root.right.key == 16
    assert t.root.right.red == False

    assert t.root.right.left.key == 15
    assert t.root.right.left.red == True

    assert t.root.right.right.key == 17
    assert t.root.right.right.red == True

def test_delete():

    t = RBTree()

    t.insert(10)
    t.insert(5)
    t.insert(15)
    t.insert(16)
    t.insert(17)

    t.delete_key(10)
    assert t.root.key == 15
    assert t.root.red == False
    assert t.root.left.key == 5
    assert t.root.left.red == False
    assert t.root.right.key == 16
    assert t.root.right.red == False
    assert t.root.right.right.key == 17
    assert t.root.right.right.red == True

    t.delete_key(15)
    assert t.root.key == 16
    assert t.root.red == False
    assert t.root.left.key == 5
    assert t.root.left.red == False
    assert t.root.right.key == 17
    assert t.root.right.red == False

    t.delete_key(18) # attempt to delete non-existing node does not change a tree and it nodes
    assert t.root.key == 16
    assert t.root.red == False
    assert t.root.left.key == 5
    assert t.root.left.red == False
    assert t.root.right.key == 17
    assert t.root.right.red == False