import graph.coloring.generate as generate
import unittest

class GenerateTestCase(unittest.TestCase):
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

    def test_generate_graph_with_chromatic_number(self):
        gwcn = generate.GenerateGraphWithChromaticNumber(16,5)
        self.assertEqual(gwcn.chromatic_number, len(gwcn.nodes))
        self.assertEqual(gwcn.chromatic_number, len(gwcn.complete_subgraph_nodes))

        for s in gwcn.nodes:
            for nodeID in s:
                node = gwcn.graph.GetNode(nodeID)
                for adj in node.GetAdjacent():
                    self.assertTrue(adj.GetID() not in s)

        for n in gwcn.complete_subgraph_nodes:
            for adj in gwcn.complete_subgraph_nodes:
                if n is not adj:
                    self.assertTrue(adj in n.GetAdjacent())
