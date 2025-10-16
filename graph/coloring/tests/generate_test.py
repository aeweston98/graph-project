import graph.coloring.generate as generate
import unittest

class ColoringTestCase(unittest.TestCase):
    def test_generate_bipartite_graph(self):
        bgraph = generate.GenerateBipartiteGraph(5)

        for nodeID in bgraph.node_sets[0]:
            node = bgraph.graph.GetNode(nodeID)
            for adj in node.GetAdjacent():
                self.assertTrue(adj.GetID() in bgraph.node_sets[1])

        for nodeID in bgraph.node_sets[1]:
            node = bgraph.graph.GetNode(nodeID)
            for adj in node.GetAdjacent():
                self.assertTrue(adj.GetID() in bgraph.node_sets[0])

