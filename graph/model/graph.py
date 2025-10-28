from typing import Dict, Set
from random import choice

class Node():
    def __init__(self, id: str):
        self.id: str = id
        self.baggage: Dict[str, str] = {}
        self.adjacent: Set['Node'] = set()

    def GetID(self) -> str:
        return self.id

    def GetBaggage(self, key: str) -> str:
        return self.baggage[key]

    def SetBaggage(self, key, value: str):
        self.baggage[key] = value

    def HasBaggage(self, key) -> bool:
        return key in self.baggage

    def AddAdjacent(self, adj):
        self.adjacent.add(adj)

    def GetAdjacent(self) -> Set['Node']:
        return self.adjacent

class Graph():
    def __init__(self):
        self.nodes: Dict[str, Node] = {}

    def GetNodes(self) -> Set[Node]:
        return set(self.nodes.values())

    def GetNode(self, id: str) -> Node:
        return self.nodes[id]

    def GetRandomNode(self) -> Node:
        # This will fail with IndexError if the node list is empty
        return choice(list(self.nodes.values()))

    def AddNode(self, node: Node):
        self.nodes[node.GetID()] = node

    def AddEdge(self, a, b: Node):
        a.AddAdjacent(b)
        b.AddAdjacent(a)
