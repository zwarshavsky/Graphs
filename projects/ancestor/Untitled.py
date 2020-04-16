def earliest_ancestor(ancestors, starting_node):
    ag = AncestorGraph()
    for parent, child in ancestors:
        ag.add_vertex(parent)
        ag.add_vertex(child)
        
    for parent,child in ancestors:
        ag.add_edge(child,parent)
    return ag.get_dist_parent(starting_node)