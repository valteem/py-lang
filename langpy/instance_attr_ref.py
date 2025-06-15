from __future__ import annotations

class Node:
    def __init__(self, key: int, pair: Node) -> None:
        self.key = key
        self.pair = pair

class ListCont():
    def __init__(self) -> None:
        self.list = []

class ListContInit():
    def __init__(self, inp = []) -> None:
        self.list = inp

class A:
    def __init__(self, attr1: int) -> None:
        self.attr1 = attr1
    def assign(self, attr2: int) -> None:
        self.attr2 = attr2