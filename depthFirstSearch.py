#################################################################################
#                         Depth First Search                                    #
# as deeply as possible, connecting as many nodes in the graph as possible      #
# and branching where necessary                                                 #
# starting and finishing times for each node display the parenthesis property   #
# all the children of a particular node in the depth first tree have            #
# a later discovery time and an earlier finish time than their parent           #
#################################################################################

from vertex import Vertex
from graph import Graph

class DFSGraph(Graph):
    """Depth First Search"""
    def __init__(self):
        """inherits from the Graph class"""
        super().__init__()
        # to keep track of the time across calls
        self.time = 0

    def dfs(self):
        """all nodes in the graph are considered and that no vertices are left out of the depth first forest"""
        vertices = [aVertex for aVertex in self]
        self.dfsHelper(vertices)
##        for aVertex in self:
##            aVertex.setColor('white')
##            aVertex.setPred(None)
##        for aVertex in self:
##            if aVertex.getColor() == 'white':
##                self.dfsvisit(aVertex)

    def dfsHelper(self, vertices):
        """all nodes in the graph are considered and that no vertices are left out of the depth first forest"""
        for v in vertices:
            v.setColor('white')
            v.setPred(None)
        for v in vertices:
            if v.getColor() == 'white':
                self.dfsvisit(v)

    def dfsvisit(self,startVertex):
        """starts with startVertex and explores all of the neighboring white vertices as deeply as possible"""
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def dfsFinishDecreasingOrder(self):
        """all nodes in the graph are considered and that no vertices are left out of the depth first forest"""
        vertices = [vert for vert in self]
        vertices.sort(key=lambda vert: vert.getFinish())
        vertices.reverse()
        self.dfsHelper(vertices)

    def transpose(self, transG):
        """transG filled as the transpose DFSGraph with Finish times where all the edges in the graph have been reversed """
        for v in self:
            addedVertex = transG.addVertex(v.getId())
            addedVertex.setFinish(v.getFinish())
        super().transpose(transG)
            

    def traverse(self,y):
        """return the path that starts at any vertex y and follow the predecessor arrows back to the root"""
        path = []
        x = y     
        while (x.getPred()):
            path.append(x.getId())
            x = x.getPred()
        path.append(x.getId())
        return path

        
