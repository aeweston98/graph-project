import graph.model.graph as model 
from typing import Set, List
import itertools
import random
import math
from dataclasses import dataclass

EDGE_RATIO = 0.75

@dataclass
class BipartiteGraph:
    graph: model.Graph
    node_sets: (Set[str], Set[str])

def GenerateBipartiteGraph(target_node_count: int) -> BipartiteGraph:
    sets = 2
    node_lists = generateNodeLists(sets, target_node_count)
    graph = model.Graph()

    addNodesToGraph(graph, list(itertools.chain.from_iterable(node_lists)))

    set_A, set_B = node_lists

    target_edges = int(len(set_A) * len(set_B) * EDGE_RATIO)

    for _ in range(target_edges):
        a = random.randrange(0, len(set_A))
        b = random.randrange(0, len(set_B))
        graph.AddEdge(set_A[a], set_B[b])
    
    return BipartiteGraph(graph, (set([node.GetID() for node in set_A]), set([node.GetID() for node in set_B])))

#def GenerateNonBipartiteGraph() -> model.Graph:


def generateNodeLists(sets: int, count: int) -> List[List[model.Node]]:
    node_lists: [List[List[model.Node]]] = [[] for _ in range(sets)]
    for id in range(count):
        node = model.Node(id)
        node_lists[(id % sets)].append(node)

    return node_lists

def addNodesToGraph(graph: model.Graph, nodes: List[model.Node]):
    for node in nodes:
        graph.AddNode(node)