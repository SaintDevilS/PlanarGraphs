import unittest
from networkx import Graph
from PlanarGraphs.min_panning_tree import MinSpanningTreeFinder
from networkx.classes.multigraph import MultiGraph

class MinSpanningTreeTester(unittest.TestCase):
    def setUp(self):
        self.MST = MinSpanningTreeFinder()
        
    def test_simple_tree(self):
        g = Graph()
        
        g.add_edge(1, 2, weight=1)
        
        min_spanning_tree = self.MST.find_min_spanning_tree(g)
        
        self.assertEqual([(1, 2)], min_spanning_tree.edges())
        
    def test_two_parallel_edges(self):
        g = MultiGraph()
        
        g.add_edge(1, 2, weight=1)
        g.add_edge(1, 2, weight=2)
        
        min_spanning_tree = self.MST.find_min_spanning_tree(g)
        
        self.assertEqual([(1, 2, {'weight': 1})], min_spanning_tree.edges(data=True))
        
        
        