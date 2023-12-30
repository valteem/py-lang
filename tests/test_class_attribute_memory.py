from langpy.class_attribute_memory import Node

def test_class_attribute_memory():

    p = Node(2, None)

    n = Node(1, p)

    n.pair.key = 3

    assert p.key == 3 # Python variables (including class attributes) act as references to a certain object

    assert id(p) == id(n.pair)

    assert hex(id(p)) == hex(id(n.pair))