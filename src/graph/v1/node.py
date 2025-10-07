from typing import Dict, Set
from .. import NodeInterface

class Node(NodeInterface):
    def __init__(self, id: str):
        self.id: str = id
        self.baggage : Dict[str, str] = {}
        self.adjacent: Set[Node]

    def GetID(self) -> str:
        return self.id

    def GetBaggage(self, key: str) -> str:
        return self.baggage[key]

    def SetBaggage(self, key, value: str):
        self.baggage[key] = value

    def AddAdjacent(self, Node):
        self.adjacent.add(Node)