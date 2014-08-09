#################################################################################
#                   Strongly Connected Components                               #
# the largest subset of vertices C such that for every pair of v,w in C         #
# we have a path from v to w and a path from w to v                             #
#################################################################################

from depthFirstSearch import DFSGraph
from queues import Queue

def stronglyConnectedComponents(g):
    """return the Strongly Connected Components of a DFSGraph g"""
    g.dfs()
    transG = DFSGraph()
    g.transpose(transG)
   
    transG.dfsFinishDecreasingOrder()
   
    # dict of path per vertex
    pathDict = {}
    for vert in transG:
        pathDict[vert.getId()] = transG.traverse(vert)
    print( pathDict)

    sccList = []
    seen = set()
    q = Queue()
    vertices = [vert for vert in transG]
    vertices.sort(key=lambda vert: vert.getFinish())
    vertices.reverse()
    for vert in vertices:
        print(vert.getId())
        if vert in seen:
            continue
        q.enqueue(vert)
        scc = set()
        while (not q.isEmpty()):
            x = q.dequeue()
            seen.add(x)
            scc.add(x.getId())
            for v in x.getConnections():
                if v.getPred() == x:
                    q.enqueue(v)
        sccList.append(scc)
    return sccList
        
    

##################
# Main() to test #
##################
if __name__ == '__main__':
    g = DFSGraph()
    for i in range(9):
        g.addVertex(i)
    g.addEdge(0,1,5)
    g.addEdge(0,2,2)
    g.addEdge(1,3,4)
    g.addEdge(1,5,4)
    g.addEdge(1,8,4)
    g.addEdge(2,3,3)
    g.addEdge(3,0,3)
    g.addEdge(3,7,4)
    g.addEdge(4,5,3)
    g.addEdge(4,7,3)
    g.addEdge(5,6,3)
    g.addEdge(6,4,3)
    g.addEdge(7,8,3)
    g.addEdge(8,7,3)
    pathList = stronglyConnectedComponents(g)
    print (pathList)

     
            
                    
    
