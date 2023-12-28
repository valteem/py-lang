"""
Somewhat naive implemetation of tree data structure
"""

from __future__ import annotations
from typing import Any
from typing import List

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
        """
#        if self.search(self.root, key) != None:
        if self.search_iterative(self.root, key) != None:
            return # nothing to add if the key already exists
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

    
    def search(self, node: Node, key: Any) -> [Node, None]:
        """
        recursive search
        """

        if node == None or key == node.key:
            return node
        else:
            if key < node.key:
                return self.search(node.left, key) # https://stackoverflow.com/questions/36488439/python-not-defined-recursive-function
            else:
                return self.search(node.right, key)
            
    
    def search_iterative(self, node: Node, key: Any) -> [Node, None]:
        """
        iterative search
        --------
        https://stackoverflow.com/a/73504415 no 'comparable' type in Python, hence typing.Any for **key**
        """
        if node == None or key == node.key:
            return node
        current_node = node
        while current_node != None and key != current_node.key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node
    

    def minimum(self, node: Node) -> Node:
        """
        returns node with minimum key, not minimum key itself
        """
        current_node = node
        while current_node.left != None:
            current_node = current_node.left
        return current_node
    

    def maximum(self, node: Node) -> Node:
        """
        returns node with maximum key, not maximum key itself
        """
        current_node = node
        while current_node.right != None:
            current_node = current_node.right
        return current_node


    def minimum_recursive(self, node: Node) -> Node:
        if node.left == None:
            return node
        else:
            return self.minimum_recursive(node.left)


    def maximum_recursive(self, node: Node) -> Node:
        if node.right == None:
            return node
        else:
            return self.maximum_recursive(node.right)


    def next_node(self, node: Node) -> Node:
        """
        returns succesor node for a given tree node, None if absent
        """
        if node.right != None:
            return self.minimum(node.right)
        parent_node = node.parent
        right_node = node
        while parent_node != None and right_node == parent_node.right:
            """
            second condition breaks traversal if **node** is left child of its parent
            """ 
            right_node = parent_node
            parent_node = parent_node.parent
        return parent_node


    def prev_node(self, node: Node) -> Node:
        """
        returns predecessor node for a given tree node, None if absent
        """
        if node.left != None:
            return self.maximum(node.left)
        parent_node = node.parent
        left_node = node
        while parent_node != None and left_node == parent_node.left:
            left_node = parent_node
            parent_node = parent_node.parent
        return parent_node
    

    def inorder_walk(self, node: Node) -> List[Any]:
        """
        inorder walk implementation with stack (list)
        """
        current = node
        stack = []
        output = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                output.append(current.key)
                current = current.right
            else:
                break
        return output
