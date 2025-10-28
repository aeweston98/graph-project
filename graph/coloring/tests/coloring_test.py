import unittest
import graph.coloring.generate as generate
import graph.coloring.color as color
import graph.coloring.dsatur as dsatur

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

class DSaturColoringNaiveTestCase(unittest.TestCase):
    def test_dsatur_coloring_bipartite(self):
        bgraph = generate.GenerateBipartiteGraph(100)
        coloring = dsatur.DSaturColoringNaive(bgraph.graph)

        self.assertEqual(coloring.colors, 2)

    def test_dsatur_coloring_valid(self):
        target_cn = 4
        test_graph = generate.GenerateGraphWithChromaticNumber(40, target_cn)
        coloring = dsatur.DSaturColoringNaive(test_graph.graph)

        # make sure we got a valid coloring
        for s in coloring.nodes:
            for nodeID in s:
                node = test_graph.graph.GetNode(nodeID)
                for adj in node.GetAdjacent():
                    self.assertTrue(adj.GetID() not in s)

        self.assertTrue(coloring.colors >= target_cn)
        print(test_graph.nodes)
        print(coloring.nodes)
