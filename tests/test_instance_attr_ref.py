from langpy.instance_attr_ref import Node, ListCont, ListContInit

def test_instance_attr_ref():

    p = Node(2, None)
    n = Node(1, p)
    n.pair.key = 3
    assert p.key == 3 # 'p' and 'n.pair' (and, hence, 'p.key' and 'n.pair.key') refer to the same object in memory
    assert id(p) == id(n.pair)
    assert hex(id(p)) == hex(id(n.pair))


    lc1 = ListCont()
    lc1.list.append(1)
    lc2 = ListCont()
    assert lc2.list == []

    """
    https://pythonforthelab.com/blog/mutable-and-immutable-attributes-of-classes/
    """
    lci1 = ListContInit() # empty 'inp' list silently instantiated here
    lci1.list.append(1)   # since 'inp' and lci1.list refer to the same object in memory, inp also changes to [1]
    lci2 = ListContInit() # inp = [1] is an input variable while constructing 'lci2'
    assert lci2.list == [1] # magic