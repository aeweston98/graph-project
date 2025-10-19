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
    nodes: (Set[str], Set[str])

def GenerateBipartiteGraph(target_node_count: int) -> BipartiteGraph:
    sets = 2
    node_lists = generateNodeLists(sets, target_node_count)
    graph = model.Graph()
    addNodesToGraph(graph, list(itertools.chain.from_iterable(node_lists)))

    set_A, set_B = node_lists

    addEdgesBetweenSets(graph, (set_A, set_B))
    
    return BipartiteGraph(graph, (set([node.GetID() for node in set_A]), set([node.GetID() for node in set_B])))

def GenerateNonBipartiteGraph(target_node_count: int) -> model.Graph:
    # target_node_count must be at least 3
    if target_node_count < 3:
        raise ValueError("target_node_count must be at least 3")

    sets = 2
    node_lists = generateNodeLists(sets, target_node_count)
    graph = model.Graph()
    addNodesToGraph(graph, list(itertools.chain.from_iterable(node_lists)))

    set_A, set_B = node_lists

    addEdgesBetweenSets(graph, (set_A, set_B))
    
    for node in set_A:
        if len(node.GetAdjacent()) == 0:
            b = random.randrange(0, len(set_B))
            graph.AddEdge(node, set_B[b])

    for node in set_B:
        if len(node.GetAdjacent()) == 0:
            a = random.randrange(0, len(set_A))
            graph.AddEdge(set_A[a], node)

    if len(set_A) >= 2:
        graph.AddEdge(set_A[0], set_A[1])
    elif len(set_B) >= 2:
        graph.AddEdge(set_A[0], set_A[1])

    return graph

def addEdgesBetweenSets(graph: model.Graph, nodes: (List[model.Node], List[model.Node])):
    set_A, set_B = nodes

    target_edges = int(len(set_A) * len(set_B) * EDGE_RATIO)

    for _ in range(target_edges):
        a = random.randrange(0, len(set_A))
        b = random.randrange(0, len(set_B))
        graph.AddEdge(set_A[a], set_B[b])
    
    return

def generateNodeLists(sets: int, count: int) -> List[List[model.Node]]:
    node_lists: [List[List[model.Node]]] = [[] for _ in range(sets)]
    for id in range(count):
        node = model.Node(id)
        node_lists[(id % sets)].append(node)

    return node_lists

def addNodesToGraph(graph: model.Graph, nodes: List[model.Node]):
    for node in nodes:
        graph.AddNode(node)