##########################################################################
#                         Prim's Algorithm                               #
# Minimum Spanning Tree                                                  #
##########################################################################

from dheap import HeapItem, DHeapHandler

class Prim:
    """Prim algorithm to find the minimum spanning tree"""
    def __init__(self, weightedEdges, root):
        """set of 3-uples (u,v,weight) and root of the search"""
        self.root = root
        # Adjacency Lists
        self.dictAdj = dict()
        for u,v,w in weightedEdges:
            # vertex u
            self._addEdgeAndWeight(u, v, w)
            # vertex v
            self._addEdgeAndWeight(v, u, w)
        # Build an empty dHeap using a DHeapHandler
        self.heapHandler =  DHeapHandler()
        self.heap = self.heapHandler.makeheap([])
        # HeapItem dictionary
        self.dictHeapItems = dict()
        for x in self.dictAdj.keys():
            if x != self.root:
                hi = self.heapHandler.heapinsert(float('inf'), x, self.heap)
            else:
                hi = self.heapHandler.heapinsert(0, self.root, self.heap)
            self.dictHeapItems[x] = hi

    def _addEdgeAndWeight(self, u, v, w):
        """add the edge (u,v) with weight w to adjacency list of u + the parent of u"""
        edges, weigth = self.dictAdj.get(u,[set(),None])
        edges |= {(v,w)}
        self.dictAdj[u] = [edges, None]

    def getMinimumSpanningTree(self):
        """return the edges of the minimum spanning tree"""
        while (len(self.heap) > 0):
            # extract the minimum vertex not already considered and marked it as not present in heap with a position at None
            hi = self.heapHandler.deletemin(self.heap)
            hi.pos = None
            for v,w in self.dictAdj[hi.item][0]:
                if self.dictHeapItems[v].pos != None and w < self.dictHeapItems[v].key:
                    # u is the new parent of v
                    self.dictAdj[v][1] = hi.item
                    self.heapHandler.heap_decreasekey(self.dictHeapItems[v], w, self.heap)
        # the edges and the weights
        mst = set()    
        for x in self.dictAdj.keys():
            if x != self.root:
                mst.add((self.dictAdj[x][1],x,self.dictHeapItems[x].key))
        return mst
        

            
##################
# Main() to test #
##################
if __name__ == '__main__':
    G = {('a','b',4), ('a','h',8), ('b','h',11), ('b','c',8), ('h','i',7), ('h','g',1), ('i','c',2),('i','g',6), ('c','d',7), ('c','f',4), ('g','f',2), ('d','f',14), ('d','e',9), ('f','e',10)}
    print(sorted(Prim(G, 'a').getMinimumSpanningTree()))
        
        

