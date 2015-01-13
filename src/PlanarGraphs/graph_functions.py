
def contract_edges(G,nodes, new_node, attr_dict=None, **attr):
    '''Contracts the edges of the nodes in the set "nodes" '''
    #Add the node with its attributes
    G.add_node(new_node, attr_dict, **attr)
    #Create the set of the edges that are to be contracted
    cntr_edge_set = G.edges(nodes, data = True)
    #Add edges from new_node to all target nodes in the set of edges that are to be contracted
    #Possibly also checking that edge attributes are preserved and not overwritten, 
    #especially in the case of an undirected G (Most lazy approach here would be to return a 
    #multigraph so that multiple edges and their data are preserved)
    G.add_edges_from(map(lambda x: (new_node,x[1],x[2]), cntr_edge_set)) 
    #Remove the edges contained in the set of edges that are to be contracted, concluding the contraction operation
    G.remove_edges_from(cntr_edge_set)
    #Remove the nodes as well
    G.remove_nodes_from(nodes)
    #Return the graph
    return G
