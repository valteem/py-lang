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
        self.root = None

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