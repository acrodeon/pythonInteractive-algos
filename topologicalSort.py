#####################################################################################
#                              Topological Sort                                     #
# takes a directed acyclic graph and produces a linear ordering of all its vertices #
# such that if the graph G contains an edge (v,w) then the vertex v comes before    #
# the vertex w in the ordering                                                      #
#####################################################################################

# from depthFirstSearch import DFSGraph

def topologicalSort(g):
    """return list of vertices sorted according to topological sort of a directed acyclic graph g"""
    # Depth First Search to compute finish time for each vertex of g as DFSGraph
    g.dfs()
    # vertices in a list in decreasing order of finish time
    vertices = [vert for vert in g]
    vertices.sort(key=lambda vert: vert.getFinish())
    return vertices
    
    
