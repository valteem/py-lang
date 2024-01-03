"""
Pure Python radix tree implementation
----------------
Adapted from https://code.google.com/archive/p/python-radix-tree/
----------------
Radix tree as opposed to trie is explained [here](https://stackoverflow.com/a/14708989)
"""

class RadixTreeNode():
    """
    There is mix of 'node' and 'edge' concepts in most radix tree definitions

    Generally speaking, keys are associated with edges.
    Nodes are intended to be build paths combining several consecutive edges into a word.
    Node (internal) may also include a flag, showing that a path producing a string terminates here.

    This implementation does not distinguish between nodes and edges. Every node is thought of as containing
    both a string (associated with an imaginary 'edge' between this node and its parent) and a termination flag
    """
    def __init__(self) -> None:
        self.key = ""
        self.children = [] # child nodes stored in a list
        self.real = False  # (?) string termination flag
        self.value = None  # (?)

    def get_number_of_matching_characters(self, key: str) -> int:
        """Compares radix tree node key and input string

        Args:
            key: input string

        Returns:
           Number of matching characters between node key and input string.
           Example:
           Let self.key = "abc", key = "abklm". Number of metching characters is 2 ("ab")       
        """
        number_of_matching_characters = 0

        while number_of_matching_characters < len(key) and number_of_matching_characters < len(self.key):
            if key[number_of_matching_characters] != self.key[number_of_matching_characters]:
                break
            number_of_matching_characters += 1

        return number_of_matching_characters
    
class DuplicareKeyError(Exception):
    """
    Key to be added already in the tree
    """
    pass

class RadixTree():
    def __init__(self) -> None:
        self.root = RadixTreeNode() # empty root node
        self.size = 0

    def insert(self, key, value, node = None) -> None:
        """Inserts key recursively

        Args:
            key: new (?) key to be inserted
            value: (?) payload
            node: (?) starting position in the tree
        """

        if not node:
            node = self.root
            self.size += 1

        number_of_matching_chars = node.get_number_of_matching_characters(key)

        # Last clause in AND is probably a misprint, number of matching chars cannot be greater
        # than length of node key
        if node.key == "" or number_of_matching_chars == 0 or (
        number_of_matching_chars < len(key) and number_of_matching_chars >= len(node.key)):
            # probably means that we need to jump to an existing child node,
            # or to create a new one
            flag = False
            new_text = key[number_of_matching_chars:]
            for child in node.children:
                if child.key.startswith(new_text[0]):
                    flag = True
                    self.insert(new_text, value, child)
                    break
            
            if not flag:
                n = RadixTreeNode()
                n.key = new_text
                n.real = True
                n.value = value
                node.children.append(n)

        elif number_of_matching_chars == len(key) and number_of_matching_chars == len(node.key):
            # exact match - converting current node to 'data node' (node.real = True)
            if node.real:
                raise DuplicareKeyError("Duplicate key: '%s' for value: '%s' " % (key, node.value))
            
            node.real = True
            node.value = value

        elif number_of_matching_chars > 0 and number_of_matching_chars < len(node.key):
            """
            Example 1:
            node.key = "abcklm", key = "abcuvw"
            0 < number_of_matching_characters = 3 < 6 = len(node.key)
            n1.key = "klm"
            node.key = "abc"
            n2.key = "uvw", 
            node.children = [..., n1, n2]

            Example 2:
            node.key = "abcklm", key = "ab", number_of_matching_characters = 2
            n1.key = "cklm"
            node.key = "ab", node.real = True
            node.children = [..., n1]
            """
            n1 = RadixTreeNode()
            n1.key = node.key[number_of_matching_chars:]
            n1.real = node.real
            n1.value = node.value
            n1.children = node.children

            node.key = key[0:number_of_matching_chars]
            node.real = False # it's Example 1 by default, can change later
            node.children = [n1]

            if number_of_matching_chars < len(key):
                n2 = RadixTreeNode()
                n2.key = key[number_of_matching_chars:]
                n2.real = True
                n2.value = value
                node.children.append(n2)
            else:
                node.value = value # Example 2
                node.real = True

        else:
            """
            TODO: example(s)
            """
            n = RadixTreeNode()
            n.key = node.key[number_of_matching_chars:]
            n.children = node.children # looks like just a split of existing key
            n.real = node.real
            n.value = node.value

            node.key = key
            node.real = True
            node.value = value
            node.children.append(n)

    def _debug_node(self, lst, level: int, node: RadixTreeNode) -> None:
        """Recursive utility method to generate visual tree

        Args:
            lst: list of visual presentations for every node in tree
            level: hierarchy level of depicted node
            node: tree node to be included in visual presentation

        Returns:
            Nothing. All magic is about adding things to 'lst'
        """

        tmp = " " * level
        tmp += "|"
        tmp += "-" * level

        if node.real:
            tmp += "%s[%s]" % (node.key, node.value)
        else:
            tmp += "%s" % (node.key)

        lst.append(tmp)

        for child in node.children:
            self._debug_node(lst, level + 1, child)
    
    def debug(self):
        """Returns string representation of the tree
        """

        lst = []
        self._debug_node(lst, 0, self.root)
        return "\r".join(lst)