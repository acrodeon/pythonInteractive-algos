#################################################################################
#                         Vertex                                                #
# represents each vertex in the graph                                           #                      
#################################################################################

class Vertex:
    """vertex in the graph"""
    def __init__(self,key):
        """key is typically a string"""
        self.id = key
        # dictionary to keep track of the vertices to which it is connected, and the weight of each edge
        self.connectedTo = {}
        # distance
        self.distance = 0
        # predecessor
        self.predecessor = None
        # color ('white' by default)
        self.color = 'white'
        # number of steps in the algorithm before vertex is first encountered
        self.discovery = 0
        # number of steps in the algorithm before a vertex is colored black
        self.finish = 0

    def addNeighbor(self,nbr,weight=0):
        """add a connection from this vertex to another"""
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """return (dict_keys type) all of the vertices that vertex is connected to"""
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        """return the weight of the edge from this vertex to the vertex passed as a parameter"""
        return self.connectedTo[nbr]

    def setDistance(self, dist):
        """set the distance to another vertex"""
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPred(self, predVertex):
        """add the predecessor vertex"""
        self.predecessor = predVertex

    def getPred(self):
        """return the predecessor vertex"""
        return self.predecessor

    def setColor(self, col):
        """set the color of the vertex"""
        self.color = col

    def getColor(self):
        """return the color of the vertex"""
        return self.color

    def setDiscovery(self, time):
        """set the number of steps in the algorithm before vertex is first encountered"""
        self.discovery = time

    def getDiscovery(self):
        """return the number of steps in the algorithm before vertex is first encountered"""
        return self.discovery

    def setFinish(self, time):
        """set the number of steps in the algorithm before a vertex is colored black"""
        self.finish = time

    def getFinish(self):
        """return the number of steps in the algorithm before a vertex is colored black"""
        return self.finish



    
