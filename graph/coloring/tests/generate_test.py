import graph.coloring.generate as generate
import unittest

class ColoringTestCase(unittest.TestCase):
    def test_generate_bipartite_graph(self):
        bgraph = generate.GenerateBipartiteGraph(5)

        self.assertEqual(len(bgraph.nodes[0].intersection(bgraph.nodes[1])), 0)

        for nodeID in bgraph.nodes[0]:
            node = bgraph.graph.GetNode(nodeID)
            for adj in node.GetAdjacent():
                self.assertTrue(adj.GetID() in bgraph.nodes[1])

        for nodeID in bgraph.nodes[1]:
            node = bgraph.graph.GetNode(nodeID)
            for adj in node.GetAdjacent():
                self.assertTrue(adj.GetID() in bgraph.nodes[0])

    def test_generate_non_bipartite_graph_invalid_input(self):
        with self.assertRaises(ValueError):
            generate.GenerateNonBipartiteGraph(1)

    def test_generate_non_bipartite_graph(self):
        nbgraph = generate.GenerateNonBipartiteGraph(10)
