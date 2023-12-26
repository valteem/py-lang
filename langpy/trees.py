"""
Somewhat naive implemetation of tree data structure
"""

class Tree:

    class Node:
        def __init__(self, key) -> None:
            self.key = key
            self.parent = None
            self.left = None
            self.right = None
    
    def __init__(self, root = None) -> None:
        self.root = root
    
    def insert(self, key) -> None:
        """
        We perform **insert** operation on keys, creating new nodes as convenient
        --------
        TODO (?): check whether key to insert is already in the tree
        """
        n = Tree.Node(key)
        parent_node = None
        current_node = self.root # start looking for appropriate place to insert new node from root node
        while current_node != None:
            parent_node = current_node
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        n.parent = parent_node
        if parent_node == None: # tree is empty
            self.root  = n
        elif key < parent_node.key:
            parent_node.left = n
        else:
            parent_node.right = n