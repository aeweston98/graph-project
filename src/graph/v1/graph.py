from .. import GraphInterface, NodeInterface, EdgeInterface
from typing import Dict, Set
from random import choice

class Graph(GraphInterface):
    def __init__(self):
        self.nodes: Dict[str, NodeInterface] = {}
        self.edges: Set[EdgeInterface] = set()

    def GetNode(self, id: str) -> NodeInterface:
        return self.nodes[id]

    def GetRandomNode(self) -> NodeInterface:
        return choice(list(self.nodes.values()))
