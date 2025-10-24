import graph.model.graph as model
from dataclasses import dataclass
from typing import List, Set

@dataclass
class Coloring:
    colors: int
    nodes: List[Set[str]]

def TwoColoring(graph: model.Graph) -> Coloring:
    colors = 2
    nodes = [set() for _ in range(colors)]
    coloring = Coloring(colors, nodes)

    def GetOppositeColor(color: int) -> int:
        if color == 1:
            return 0
        else:
            return 1

    def Color(node: model.Node, coloring: Coloring, color: int) -> bool:
        opp_color = GetOppositeColor(color)
        if node.GetID() in coloring.nodes[color]:
            return True
        elif node.GetID() in coloring.nodes[opp_color]:
            return False

        coloring.nodes[color].add(node.GetID())

        for adj in node.GetAdjacent():
            if not Color(adj, coloring, opp_color):
                return False
        
        return True

    valid_color_exists = Color(graph.GetRandomNode(), coloring, 0)

    if not valid_color_exists:
        raise ValueError("no two-coloring exists for the graph")

    return coloring
