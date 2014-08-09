#################################################################################
#                          Dijkstra’s Algorithm                                 #
# iterative algorithm that provides us with the shortest path                   #
# from one particular starting node to all other nodes in the graph             #
# Works only when the edge weights are all positive                             #
#################################################################################

import sys
from vertex import Vertex
from graph import Graph
from stack import Stack

class DijkstraHeap:
    """Min Heap for every [key,x] with parent p, the key in p is smaller than or equal to the key in x"""
    def __init__(self):
        """creates a new, empty, binary heap"""
        # a single zero as the first element of heapList not used, but is there so that simple integer division 
        self.heapList = [[0,None]]
        self.currentSize = 0

    def minChild(self,i):
        """returns the position of the minimum child (at least left child exists)"""
        if i * 2 + 1 > self.currentSize:
            # no right child thus return position of left child
            return i * 2
        elif self.heapList[i*2][0] < self.heapList[i*2+1][0]:
            return i * 2
        else:
            return i * 2 + 1
        
    def percUp(self,i):
        """to keep heap min property from bottom to top"""
        while i // 2 > 0:
            #at 0, we are the 0 non considered position
            if self.heapList[i][0] < self.heapList[i // 2][0]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    def percDown(self,i):
        """to keep heap min property from top to bottom"""
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i][0] > self.heapList[mc][0]:
                self.heapList[i] , self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def insert(self,k, vertex):
        """adds a new [k,vertex] to the heap"""
        self.heapList.append([k,vertex])
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        """returns the [key,vertex] with the minimum key value, removing the item from the heap"""
        retval = self.heapList[1]
        # replace by the last element
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        # remove the last item as it is in first position
        self.heapList.pop()
        # recover heap min property from top to bottom
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        """builds a new heap from a list of [key,vertex]"""
        # half of the heap because from i+1 ... nodes are leaves
        i = len(alist) // 2
        self.currentSize = len(alist)
        # by design, the first element 0 is not considered
        self.heapList = [[0,None]] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


    def decreaseKey(self, nextVert,newDist):
        """replaces [key,nextVert] by [newDist,nextVert] and keeps min heap structure"""
        i = 1
        while (i <= self.currentSize):       
            if self.heapList[i][1] == nextVert:
                self.heapList[i][0] = newDist
                self.percUp(i)
                break
            else:
                i += 1
                
    def isEmpty(self):
        """returns True if no [key,vertex] is stored"""
        return self.currentSize == 0


class DijkstraAlgo:
    """Iterative Dijkstra’s Algorithm"""
    def __init__(self, G):
        """G is the (positively) weighted graph, all vertices are initialised at infinity distance"""
        self.G = G
        for vert in self.G:
            vert.setDistance(sys.maxsize)

    def computeShortPaths(self, startVertex):
        """compute the shortest paths from startVertex"""
        pq = DijkstraHeap()
        startVertex.setDistance(0)
        pq.buildHeap([[v.getDistance(),v] for v in self.G])
        while not pq.isEmpty():
            # iterates once for every vertex in the graph
            currentVert = (pq.delMin())[1]  
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert,newDist)

    def printShortPaths(self):
        """For each vertex, print the shortest paths from a same start vertex"""
        s = Stack()
        for vert in self.G:          
            x = vert
            s.push(x)
            print("Shortest path to reach {}".format(x.getId()))
            while (x.getPred()):
                s.push(x.getPred())
                x = x.getPred()
            while not s.isEmpty():
                print((s.pop()).getId(), end =' ')
            print()
        
                
##################
# Main() to test #
##################
if __name__ == '__main__':
    g = Graph()
    for i in range(1, 7):
        g.addVertex(i)
    g.addEdge(1,2,2)
    g.addEdge(1,5,1)
    g.addEdge(2,3,3)
    g.addEdge(2,5,2)
    g.addEdge(3,4,5)
    g.addEdge(3,6,1)
    g.addEdge(5,6,1)
    g.addEdge(6,4,1)

    dijAlgo = DijkstraAlgo(g)
    dijAlgo.computeShortPaths(g.getVertex(1))
    dijAlgo.printShortPaths()
    
    
    
    

