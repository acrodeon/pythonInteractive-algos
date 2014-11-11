#################################################################################
#                         Ford-Fulkerson O(S * |Flot_max|)                      #
# Find a maximum flow in a flow network                                         #                      
#################################################################################

# to help finding a min value in a list of 2-uples accordind to the second element order
from operator import itemgetter

class Edge:
    """An edge with a capacity >=0"""

    def __init__(self, u, v, c):
        """Initialize the endpoints of the edge and its capacity"""
        assert(c >= 0)
        self.u = u
        self.v = v
        self.c = c
        
    def getCapacity(self):
        """return the capacity of the edge"""
        return self.c

    def getEndPoints(self):
        """return the 2-uple of the endpoints"""
        return (self.u, self.v)

    def getDestination(self):
        """return the destination vertex of the edge"""
        return self.v

    def getSource(self):
        """return the source vertex of the edge"""
        return self.u


class FordFulkerson:
    """A Flow network with its capacity function"""

    def __init__(self, vertices, edges):
        """ set of vertices and egdes (u,v,c)"""
        # add vertices
        self.vertices = set()
        self.adj = dict()
        for x in vertices:
            self._addVertex(x)
        # add edges
        self._edgesEndPoints = set()
        for u,v,c in edges:
            self._addEdge(u,v,c)
        # add reverse edge of existing edge if not already present
        self._addMissingReverseEdge()
        # the flow function as dictionary with edges as key
        self.flow = dict()

    def maxFlow(self, s, t):
        """return a maximum flow from s to t"""
        self._initializeFlow()
        improvingPath = self._findPathInResidualNetwork(s,t)
        while(improvingPath != None):
            pathCapacity = min(improvingPath, key=itemgetter(1))[1] 
            for edge,residualCapacity in improvingPath:
                u,v = edge.getEndPoints()
                self.flow[(u,v)] += pathCapacity
                self.flow[(v,u)] -= pathCapacity
            improvingPath = self._findPathInResidualNetwork(s,t)
        return sum(self.flow[edge.getEndPoints()] for edge in self.adj[s])

    def _addVertex(self, x):
        """Add the vertex x to the graph"""
        self.vertices.add(x)
        if x not in self.adj:
            self.adj[x] = []

    def _addEdge(self, u, v, c):
        """Add an edge (u,v) with a capacity c and its reverse edge (v,u) with capacity. Parallel edges are not supported"""
        edge_uv = Edge(u,v,c)
        if (u,v) not in self._edgesEndPoints:
            if u not in self.vertices:
                self._addVertex(u)
            if v not in self.vertices:
                self._addVertex(v)
            self.adj[u].append(edge_uv)
            self._edgesEndPoints.add((u,v))
            
    def _addMissingReverseEdge(self):
        """Add a reverse edge (v,u,0) for an existing (u,v,c) edge if (v,u) not explicitly defined in flow network"""
        for edges in self.adj.values():
            for edge in edges:
                u,v = edge.getEndPoints()
                self._addEdge(v,u,0)       
        
    def _initializeFlow(self):
        """Set to 0 each flows associtiated to each edge's endpoints"""
        for edges in self.adj.values():
            for edge in edges:
                self.flow[edge.getEndPoints()] = 0

    def _findPathInResidualNetwork(self, s, t, path=[]):
        """find a path as list from s to t in residual network based on http://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm"""
        if s == t:
            return path
        for edge in self.adj[s]:
            residualCapacity = edge.getCapacity() - self.flow[edge.getEndPoints()]
            if residualCapacity > 0 and not (edge, residualCapacity) in path:
                improvingPath = self._findPathInResidualNetwork(edge.getDestination(), t, path + [(edge, residualCapacity)])
                if improvingPath != None:
                    return improvingPath

                
##################
# Main() to test #
##################
if __name__ == '__main__':
    vertices = {'s', 'v1', 'v2', 'v3', 'v4', 't'}
    edges = {('s','v1',16),('s','v2',13),('v1','v2',10),('v1','v3',12),('v2','v1',4),('v2','v4',14),('v3','v2',9),('v3','t',20),('v4','v3',7),('v4','t',4)}
    FordFulkerson = FordFulkerson(vertices, edges)
    print(FordFulkerson.maxFlow('s', 't'))
    
    
    
        
