import graph.model.graph as model 
from typing import Set
import itertools

def GenerateBipartiteGraph(nodeCount: int) -> model.Graph:
    sets = 2
    node_lists = generateNodeLists(sets, count)
    graph = model.Graph()

    addNodesToGraph(graph, list(itertools.chain.from_iterable(node_lists)))

    setA, setB = node_lists
    for i in range()
    
    return graph

def GenerateNonBipartiteGraph() -> model.Graph:


def generateNodeLists(sets: int, count: int) -> List[List[model.Node]]:


def addNodesToGraph(graph: model.Graph, nodes: List[model.Node]):
    for node in nodes:
        graph.AddNode(node)