from __future__ import annotations

from langpy.trees import Tree

"""
CLRS based implementation of red-black tree
"""

class Node():
    def __init__(self, key, value = None, red: bool = True) -> None:
        self.key = key
        self.value = value
        self.red = red
        self.parent = None
        self.left = None
        self.right = None


class RBTree():
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
        xnode = ynode.left
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
                ynode = rnode.parent.parent.right
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
        node = Node(key, value) # new node for any unique key
        node.left, node.right = self.dummy, self.dummy
        ynode = self.dummy
        xnode = self.root
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