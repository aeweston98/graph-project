import graph.model.graph as model
import graph.coloring.color as color
from typing import Dict, Set
from collections import defaultdict

COLOR_BAGGAGE_TAG = "color"

def DSaturColoringNaive(graph: model.Graph) -> color.Coloring:
    saturation_per_node = {}
    uncolored_neigbours = {}

    greatest_used_color = 0

    for node in graph.GetNodes():
        uncolored_neigbours[node.GetID()] = len(node.GetAdjacent())
        saturation_per_node[node.GetID()] = set()

    while len(uncolored_neigbours) > 0:
        cand_id = getNextNode(saturation_per_node, uncolored_neigbours)
        cand = graph.GetNode(cand_id)

        assigned_color = getMinUnusedColor(cand)
        greatest_used_color = max(greatest_used_color, assigned_color)
        cand.SetBaggage(COLOR_BAGGAGE_TAG, str(assigned_color))

        for adj in cand.GetAdjacent():
            if adj.HasBaggage(COLOR_BAGGAGE_TAG):
                continue
            uncolored_neigbours[adj.GetID()] -= 1
            saturation_per_node[adj.GetID()].add(assigned_color)

        del uncolored_neigbours[cand_id]
        del saturation_per_node[cand_id]

    colors = [set() for _ in range(greatest_used_color+1)]
    for node in graph.GetNodes():
        colors[int(node.GetBaggage(COLOR_BAGGAGE_TAG))].add(node.GetID())

    return color.Coloring(greatest_used_color + 1, colors)

def getNextNode(saturation_per_node: dict, uncolored_neigbours: dict) -> str:
    cand = ""

    for node_id in saturation_per_node.keys():
        if cand == "":
            cand = node_id
        elif saturation_per_node[node_id] > saturation_per_node[cand]:
            cand = node_id
        elif saturation_per_node[node_id] == saturation_per_node[cand] and uncolored_neigbours[node_id] > uncolored_neigbours[cand]:
            cand = node_id

    return cand

def getMinUnusedColor(node: model.Node) -> int:
    colors_seen = set()
    for adj in node.GetAdjacent():
        if adj.HasBaggage(COLOR_BAGGAGE_TAG):
            color = int(adj.GetBaggage(COLOR_BAGGAGE_TAG))
            colors_seen.add(color)
    
    colors_seen = list(colors_seen)
    colors_seen.sort()
    for i in range(len(colors_seen)):
        if colors_seen[i] > i:
            return i

    return len(colors_seen)

