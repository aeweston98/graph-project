import graph.model.graph as model 
from typing import Set, List
import itertools
import random
import math
from dataclasses import dataclass

BIPARTITE_GRAPH_EDGE_RATIO = 0.75

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

    target_edges = int(len(set_A) * len(set_B) * BIPARTITE_GRAPH_EDGE_RATIO)

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

def getNodeIDSets(node_lists: List[List[model.Node]]) -> List[Set[str]]:
    return [set([node.GetID() for node in l]) for l in node_lists]    


# to do: should be consistent about using ID str vs. Node
@dataclass
class GraphWithChromaticNumber:
    graph: model.Graph
    nodes: List[Set[str]]
    complete_subgraph_nodes: List[model.Node]
    chromatic_number: int

# To generate a graph with a particular chromatic number k
# We first make k sets of nodes.
# Then we add edges from each node to a random node in every set but its own
# This guarantees that the chromatic number is at most k, but does not guarantee the chromatic
# number is exactly k - it could also be smaller.
#
# Proof by counterexample: Assume above described scheme guarantees chromatic number exactly k.
# Take graph with nodes {a, b, c, d, e, f, g, h} and edges
# {af, ah, ac, bg, be, bd, cg, ce, dh, df, eh, fg}. It satisfies the scheme
# (4 sets of nodes, edge between every node and a node in every other set), but it has a chromatic
# number of 2 - 2 coloring is 1: a, d, e, g / 2: b, c, f, h
# Therefore the above scheme does not guarantee chromatic number k.
# In order to ensure the chromatic number of the graph is k, we can take a node from each of the
# k sets and add edges so that they would form a complete graph amongst that subset of nodes.
#
# This can still result in a graph that is not connected, so a subgraph could have a smaller chromatic number.
# Could address this in the algorithm by identifying connected components and using same methodology, or by adding edges
# connect all the connected components.

def GenerateGraphWithChromaticNumber(target_node_count, chromatic_number: int) -> model.Graph:
    if target_node_count < chromatic_number:
        return ValueError("target_node_count must be at least chromatic_number")

    sets = chromatic_number
    node_lists = generateNodeLists(chromatic_number, target_node_count)

    graph = model.Graph()
    addNodesToGraph(graph, list(itertools.chain.from_iterable(node_lists)))

    complete_subgraph_nodes = [random.choice(node_set) for node_set in node_lists]

    for n in complete_subgraph_nodes:
        for adj in complete_subgraph_nodes:
            if n is adj:
                continue
            graph.AddEdge(n, adj)

    for node_set in node_lists:
        for node in node_set:
            for alt_set in node_lists:
                if alt_set is node_set:
                    continue
                for _ in range(random.randrange(0, len(alt_set)//2)):
                    i = random.randrange(0, len(alt_set))
                    graph.AddEdge(node, alt_set[i])

    return GraphWithChromaticNumber(graph, getNodeIDSets(node_lists), complete_subgraph_nodes, chromatic_number)
