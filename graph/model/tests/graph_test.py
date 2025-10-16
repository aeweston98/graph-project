import unittest
import graph.model.graph as model

class GraphTestCase(unittest.TestCase):
    def setUp(self):
        self.test_graph = model.Graph()
       
        nodeIDs = ["a", "b", "c", "d"]
        self.nodes = set()
        for id in nodeIDs:
            node = model.Node(id)
            self.nodes.add(node)

    def test_get_node_exists(self):
        for node in self.nodes:
            self.test_graph.AddNode(node)

        for node in self.nodes:
            self.assertIs(self.test_graph.GetNode(node.GetID()), node)
            self.assertTrue(self.test_graph.GetNode("a") in self.nodes)

    def test_get_random_node(self):
        for node in self.nodes:
            self.test_graph.AddNode(node)

        self.assertTrue(self.test_graph.GetRandomNode() in self.nodes)



