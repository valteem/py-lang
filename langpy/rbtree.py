# Consider using BigTree or AnyTree to avoid type checking issues

from typing import Union

from __future__ import annotations

from langpy.trees import Node as BaseNode, Tree

"""
CLRS based implementation of red-black tree
"""

class Node(BaseNode):
    def __init__(self, key, value = None, red: bool = True) -> None:
        super().__init__(key, value)
        self.red = red

class RBTree(Tree):
    """
    Red-black tree

    TODO: Inheriting utility methods from basic Tree class
    """
    def __init__(self) -> None:
        self.dummy = Node("dummy", "dummy node", False) # dummy nodes (super-root, leaves) are always black 
        self.root = self.dummy

    def rotate_left(self, xnode: Node) -> None:
        """
                   xnode                                                 ynode
                 /       \                          \                  /       \
                /         \                          \                /         \
            alpha        ynode          ============  \            xnode       gamma
                       /       \        ============  /          /       \
                      /         \                    /          /         \
                    beta      gamma                 /        alpha       beta
        """
        ynode = xnode.right
        xnode.right = ynode.left       # beta
        if ynode.left != self.dummy:
            ynode.left.parent = xnode
        ynode.parent = xnode.parent
        if xnode.parent == self.dummy: # if 'xnode' is tree root
            self.root = ynode          # then 'ynode'  becomes tree root instead
        elif xnode == xnode.parent.left:
            xnode.parent.left = ynode
        else:
            xnode.parent.right = ynode
        ynode.left = xnode
        xnode.parent = ynode

    def rotate_right(self, ynode: Node) -> None:
        """
                        ynode                                          xnode
                      /       \                       \              /       \
                     /         \                       \            /         \
                  xnode       gamma       ============  \        alpha       ynode
                /       \                 ============  /                  /       \
               /         \                             /                  /         \
            alpha       beta                          /                beta       gamma
        """
        xnode: Node = ynode.left
        ynode.left = xnode.right       # beta
        if xnode.right != self.dummy:
            xnode.right.parent = ynode
        xnode.parent = ynode.parent
        if ynode.parent == self.dummy: # if 'ynode' is tree root
            self.root = xnode          # then 'xnode' becomes tree root instead
        elif ynode.parent == ynode.parent.left:
            ynode.parent.left = xnode
        else:
            ynode.parent.right = xnode
        xnode.right = ynode
        ynode.parent = xnode

    def arrange_after_insert(self, rnode: Node) -> None:
        """
        Arrange (recolor and rotate) after inserting a new node ('rnode')
        """
        while rnode.parent.red == True: # if parent is black, there is nothing to arrange - no red-black property is broken
            if rnode.parent == rnode.parent.parent.left:
                """
                      rnode.parent.parent                                  rnode.parent.parent
                             /      \                                             /      \
                            /        \                                           /        \
                     rnode.parent   ynode             OR                  rnode.parent   ynode                     
                          /                                                      \
                         /                                                        \
                      rnode                                                      rnode
                """
                ynode: Node = rnode.parent.parent.right
                if ynode.red:
                    # recolor parent node and 'uncle node' to black, grandparent to red 
                    ynode.red = False
                    rnode.parent.red = False
                    rnode.parent.parent.red = True
                    rnode = rnode.parent.parent
                else: # uncle node is black
                    if rnode == rnode.parent.right:
                        """
                           rnode.parent.parent
                                  /      \
                                 /        \
                          rnode.parent   ynode                     
                                 \
                                  \
                                 rnode
                        """
                        rnode = rnode.parent # test_node_reassign()
                        self.rotate_left(rnode)
                    rnode.parent.red = False
                    rnode.parent.parent.red = True
                    self.rotate_right(rnode.parent.parent)
            else:
                """
                        rnode.parent.parent                rnode.parent.parent
                            /         \                        /         \
                           /           \                      /           \
                         ynode    rnode.parent    OR       ynode    rnode.parent
                                        /                                  \
                                       /                                    \
                                     rnode                                rnode
                """
                ynode = rnode.parent.parent.left
                if ynode.red:
                    ynode.red = False
                    rnode.parent.red = False
                    rnode.parent.parent.red = True
                    rnode = rnode.parent.parent
                else:
                    if rnode == rnode.parent.left:
                        """
                            rnode.parent.parent
                                /         \
                               /           \
                             ynode    rnode.parent
                                            /
                                           /
                                         rnode
                        """
                        rnode = rnode.parent
                        self.rotate_right(rnode)
                    rnode.parent.red = False
                    rnode.parent.parent.red = True
                    self.rotate_left(rnode.parent.parent)
        self.root.red = False

    def insert(self, key, value = None):
        """
        Adding new key-value pair into the tree
        ----------------

        TODO: add check if key added is already in the tree
        """
        node: Node = Node(key, value) # new node for any unique key
        node.left, node.right = self.dummy, self.dummy
        ynode: Node = self.dummy
        xnode: Node = self.root
        while xnode != self.dummy:
            ynode = xnode
            if key < xnode.key:
                xnode = xnode.left
            else:
                xnode = xnode.right
        node.parent = ynode
        if ynode == self.dummy: # root is 'self.dummy', i.e. tree is empty
            self.root = node
        else:
            if key < ynode.key:
                ynode.left = node
            else:
                ynode.right = node
        self.arrange_after_insert(node)

    def replace_node(self, node_old: Node, node_new: Node) -> None:
        if node_old.parent == self.dummy: # root node
            self.root = node_new
        else:
            if node_old == node_old.parent.left:
                node_old.parent.left = node_new
            else:
                node_old.parent.right = node_new
        node_new.parent = node_old.parent
        """
        'node.new.left' and 'node_new.right' to be set by caller
        """

    def minimum(self, node: Node) -> Node:
        if node == self.dummy:
            return None
        while node.left != self.dummy:
            node = node.left
        return node

    def arrange_after_delete(self, node: Node) -> None:
        while node != self.root and node.red == False:
            if node == node.parent.left:
                """
                Case A:
                    - 'node' is left child of its parent
                """
                wnode: Node = node.parent.right
                """
                Case A.1:
                    - 'node' right sibling 'wnode' is red
                """
                if wnode.red == True:
                    wnode.red = False # this ensures Case A.2 deals with black 'wnode' only
                    node.parent.red = True
                    self.rotate_left(node.parent)
                    wnode = node.parent.right # former node.parent.right.left
                """
                Case A.2:
                    - 'node' right sibling 'wnode' is black (output of Case A.1 provides for that)
                    - both 'wnode' children are black
                """
                if wnode.left.red == False and wnode.right.red == False:
                    wnode.red = True
                    node = node.parent
                else:
                    """
                    Case A.3:
                        - 'node' right sibling 'wnode' is black
                        - 'wnode' left child is red
                        - 'wnode' right child is black
                    """
                    if wnode.right.red == False:
                        wnode.left.red = False
                        wnode.red = True
                        self.rotate_right(wnode)
                        wnode = node.parent.right
                    """
                    Case A.4:
                        - 'node' right sibling 'wnode' is black
                        - 'wnode' right child is red
                    """
                    wnode.red = node.parent.red
                    node.parent.red = False
                    wnode.right.red = False
                    self.rotate_left(node.parent)
                    self.root = node
            else:
                """
                Case B:
                    - 'node' is right child of it parent
                """
                wnode = node.parent.left
                """
                Case B.1:
                    - 'node' left sibling 'wnode' is red
                """
                if wnode.red == True:
                    wnode.red = False # this ensures Case B.2 deals with black 'wnode' only
                    node.parent.red = True
                    self.rotate_right(node.parent)
                    wnode = node.parent.left
                """
                Case B.2:
                    - 'node' left sibling 'wnode' is black (output of Case B.1 provides for that)
                    - both 'wnode' children are black
                """
                if wnode.left.red == False and wnode.right.red == False:
                    wnode.red = True
                    node = node.parent
                else:
                    """
                    Case B.3:
                        - 'node' left sibling 'wnode' is black
                        - 'wnode' right child is red
                        - 'wnode' left child is black
                    """
                    if wnode.left.red == False:
                        wnode.right.red = False
                        wnode.red = True
                        self.rotate_left(wnode)
                        wnode = node.parent.left
                    """
                    Case B.4:
                        - 'node' left sibling 'wnode' is black
                        - 'wnode' left child is red
                    """
                    wnode.red = node.parent.red
                    node.parent.red = False
                    wnode.left.red = False
                    self.rotate_right(node.parent)
                    self.root = node
        node.red = False
    
    def replace_node(self, old: Node, new: Node) -> None:
        if old.parent == self.dummy:
            self.root = new
        elif old == old.parent.left:
            old.parent.left = new
        else:
            old.parent.right = new
        new.parent = old.parent

    def delete_node(self, node: Node) -> None:
        original_red: bool = node.red
        if node.left == self.dummy:
            xnode: Node = node.right # node to be passed to arrange_after_delete()
            self.replace_node(node, xnode)
        elif node.right == self.dummy:
            xnode = node.left
            self.replace(node, xnode)
        else: # both left and right child of deleted node are not dummies
            mnode: Node = self.minimum(node.right)
            original_red = mnode.red
            xnode = mnode.right
            if mnode.parent == node:
                xnode.parent = mnode
            else:
                self.replace_node(mnode, mnode.right)
                mnode.right = node.right
                mnode.right.parent = mnode
            self.replace_node(node, mnode)
            mnode.left = node.left
            mnode.left.parent = mnode
            mnode.red = node.red
        if original_red == False:
            self.arrange_after_delete(xnode)

    def search(self, node: Node, key) -> Union[Node, None]:
        if node == self.dummy:
            return None
        elif key == node.key:
            return node
        else:
            if key < node.key:
                return self.search(node.left, key)
            else:
                return self.search(node.right, key)
            
    def delete_key(self, key) -> None:
        n: Node = self.search(self.root, key)
        if n is not None:
            self.delete_node(n)