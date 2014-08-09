#################################################################################
#                         Knight's Tour Graph                                   #
# Each square on the chessboard can be represented as a node in the graph       #
# Each legal move by the knight can be represented as an edge in the graph      #
# O(kN), where N is the number of squares on the board, and k a small constant  #
#################################################################################

from vertex import Vertex
from graph import Graph

def knightGraph(bdSize):
    """build the full graph for a bdSize-by-bdSize chessboard"""
    ktGraph = Graph()
    for row in range(bdSize):
       for col in range(bdSize):
           # conversion of location on the board in terms of a row and a column into a linear vertex number
           nodeId = posToNodeId(row,col,bdSize)
           # list of legal moves for that position on the board
           newPositions = genLegalMoves(row,col,bdSize)
           for e in newPositions:
               nid = posToNodeId(e[0],e[1],bdSize)
               ktGraph.addEdge(nodeId,nid)
    return ktGraph

def legalCoord(x,bdSize):
    """makes sure that coord x is still on the board"""
    return (x >= 0 and x < bdSize)

def genLegalMoves(x,y,bdSize):
    """return the list of legal moves for (x,y) position on the board"""
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def posToNodeId(row,col,bdSize):
    """conversion of location on the board in terms of a row and a column into a linear vertex number"""
    return str(row * bdSize + col * bdSize)

def orderByAvail(u):
    """ return a list of vertices to go next ordered by the fewest available moves"""
    resList = []
    for v in u.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]

def knightTour(n,path,u,limit):
    """n, the current depth in the search tree; path, a list of vertices visited up to this point; u, the vertex in the graph we wish to explore; and limit the number of nodes in the path"""
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(orderByAvail(u))
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    #path is the order we need to traverse the graph to visit each node exactly once
    return done
