import unittest
import graph.coloring.generate as generate
import graph.coloring.color as color

class TwoColoringTestCase(unittest.TestCase):
    def test_two_coloring_valid(self):
        bgraph = generate.GenerateBipartiteGraph(100)
        coloring = color.TwoColoring(bgraph.graph)

        self.assertEqual(coloring.colors, 2)

        for nodeID in coloring.nodes[0]:
            node = bgraph.graph.GetNode(nodeID)
            for adj in node.GetAdjacent():
                self.assertTrue(adj.GetID() in coloring.nodes[1])

        for nodeID in coloring.nodes[1]:
            node = bgraph.graph.GetNode(nodeID)
            for adj in node.GetAdjacent():
                self.assertTrue(adj.GetID() in coloring.nodes[0])

    def test_two_coloring_invalid(self):
        test_graph = generate.GenerateNonBipartiteGraph(100)
        with self.assertRaises(ValueError):
            coloring = color.TwoColoring(test_graph)

