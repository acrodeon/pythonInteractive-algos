#################################################################################
#                         Graph                                                 #
# represents the graph abstract data type                                       #                      
#################################################################################

from vertex import Vertex

class Graph:
    """the graph abstract data type"""
    def __init__(self):
        """creates a new, empty graph"""
        # a dictionary that maps vertex names to vertex objects
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        """adds and returns an instance of Vertex to the graph"""
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        """finds and return the vertex named n in the graph or None"""
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        """True if the given vertex is in the graph, False otherwise"""
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        """adds a new (weighted) directed edge 'f' -> 't' to the graph"""
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """returns the list of all vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """to iterate over all the vertex objects in a particular graph"""
        return iter(self.vertList.values())

    def transpose(self, transG):
        """transG filled as the transpose graph where all the edges in the graph have been reversed"""
        for v in self:
            for w in v.getConnections():
                transG.addEdge(w.getId(), v.getId(), v.getWeight(w))
            
                

##################
# Main() to test #
##################
if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    print(g.vertList)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for vert in g:
        for adjVert in vert.getConnections():
            print("( %s , %s )" % (vert.getId(), adjVert.getId()))
            
    transG = Graph()
    g.transpose(transG)
    print()
    print(transG.vertList)
    for vert in transG:
        for adjVert in vert.getConnections():
            print("( %s , %s )" % (vert.getId(), adjVert.getId()))
    

