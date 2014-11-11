#################################################################################
#                         Edmonds-Karp O(S.A**2)                                #
# Find a maximum flow in a flow network                                         #                      
#################################################################################

from ford_fulkerson import FordFulkerson, Edge
from queues import Queue

WHITE = 'WHITE'
GREY = 'GREY'
BLACK = 'BLACK'
INFINITE = float('inf')

class EdmondsKarp(FordFulkerson):
    """Algorithm Edmonds-Karp is Ford-Fulkerson with Breadth First Search to find improving path in residual graph"""

    def __init__(self, vertices, edges):
        """ set of vertices and egdes (u,v,c)"""
        FordFulkerson.__init__(self, vertices, edges)
        self.color = dict()
        self.distance = dict()
        self.parentEdge = dict()
        
    def _initializeColorDistanceParent(self, s):
        """Initialize the dictionaries before each BFS"""
        for u in self.vertices:
            self.color[u] = WHITE
            self.distance[u] = INFINITE
            self.parentEdge[u] = None
        self.color[s] = GREY
        self.distance[s] = 0
                    
    def _findPathInResidualNetwork(self, s, t, path=[]):
        """find a path as list from s to t in residual network based on Breadth First Search"""
        self._initializeColorDistanceParent(s)
        queue = Queue()
        queue.enqueue(s)
        while (queue.size() > 0):
            u = queue.dequeue()
            for edge in self.adj[u]:
                v = edge.getDestination()
                if self.color[v] == WHITE:
                    residualCapacity = edge.getCapacity() - self.flow[edge.getEndPoints()]
                    if residualCapacity > 0:
                        self.color[v] = GREY
                        self.distance[v] = self.distance[u] + 1
                        self.parentEdge[v] = (edge, residualCapacity)
                        queue.enqueue(v)
            self.color[u] = BLACK
        # build improving path
        return self._buildImprovingPath(s,t)

    def _buildImprovingPath(self, s, t):
        """build improving path according to BFS execution as list of 2-uples (edge, residualCapacity)"""
        path = []
        x = t
        while (self.parentEdge[x] != None):
            path.insert(0,self.parentEdge[x])
            x = (self.parentEdge[x][0]).getSource()
        if path != [] and (path[0][0]).getSource() == s:
            return path
        return None
        
        
            
##################
# Main() to test #
##################
if __name__ == '__main__':
    vertices = {'s', 'v1', 'v2', 'v3', 'v4', 't'}
    edges = {('s','v1',16),('s','v2',13),('v1','v2',10),('v1','v3',12),('v2','v1',4),('v2','v4',14),('v3','v2',9),('v3','t',20),('v4','v3',7),('v4','t',4)}
    EdmondsKarp = EdmondsKarp(vertices, edges)
    print(EdmondsKarp.maxFlow('s', 't'))
    
            
        
        
