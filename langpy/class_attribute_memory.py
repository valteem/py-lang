from __future__ import annotations

class Node:

    def __init__(self, key: int, pair: Node) -> None:
        self.key = key
        self.pair = pair