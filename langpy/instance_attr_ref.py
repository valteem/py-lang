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