#######################################################################################################
#                                   Breadth First Search                                              #
# A white vertex is an undiscovered vertex. When a vertex is initially discovered it is colored gray, #
# and when BFS has completely explored a vertex it is colored black                                   #
# This means that once a vertex is colored black, it has no white vertices adjacent to it             #
# A gray node, on the other hand, may have some white vertices adjacent to it, indicating that        #
# there are still additional vertices to explore                                                      #                  
#######################################################################################################

from vertex import Vertex
from graph import Graph
from queues import Queue

def bfs(g,start):
    """Breadth First Search from start vertex"""
    start.setDistance(0)
    start.setPred(None)
    # start at the front of the queue
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        # explore vertices at the front of the queue
        currentVert = vertQueue.dequeue()
        # all adjacent vertices of currentVert
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    """start at any vertex y in the breadth first search tree and follow the predecessor arrows back to the root to find the shortest path"""
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


