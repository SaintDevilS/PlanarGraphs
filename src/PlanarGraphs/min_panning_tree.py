from graph_functions import contract_edges
from networkx import Graph

class MinSpanningTreeFinder:
    def __init__(self):
        self.sparsity = 3;
    
    def find_min_edge_in_adjecency_list(self, node):
        for node.
    
    def find_min_spanning_tree(self, planar_graph):
        MST_graph = Graph()
        sparse_nodes = list()
        
        for node in planar_graph.nodes():
            if len(node.neighbors()) < self.sparsity * 2:
                sparse_nodes.append(node)
                
        
        while len(sparse_nodes) != 0:
            node = sparse_nodes.pop()
            node
            
        return MST_graph