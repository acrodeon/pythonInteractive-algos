#################################################################################
#                          Binary Min Heap                                      #
# the min heap, in which the smallest key is always at the front                #
# both enqueue and dequeue items in O(log n)                                    #
#################################################################################

class BinHeap:
    """Min Heap for every node x with parent p, the key in p is smaller than or equal to the key in x"""
    def __init__(self):
        """creates a new, empty, binary heap"""
        # a single zero as the first element of heapList not used, but is there so that simple integer division 
        self.heapList = [0]
        self.currentSize = 0

    def minChild(self,i):
        """returns the position of the minimum child (at least left child exists)"""
        if i * 2 + 1 > self.currentSize:
            # no right child thus return position of left child
            return i * 2
        elif self.heapList[i*2] < self.heapList[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1
        
    def percUp(self,i):
        """to keep heap min property from bottom to top"""
        while i // 2 > 0:
            #at 0, we are the 0 non considered position
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    def percDown(self,i):
        """to keep heap min property from top to bottom"""
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i] , self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def insert(self,k):
        """adds a new item to the heap"""
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        """returns the item with the minimum key value, removing the item from the heap"""
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
        """builds a new heap from a list of keys"""
        # half of the heap because from i+1 ... nodes are leaves
        i = len(alist) // 2
        self.currentSize = len(alist)
        # by design, the first element 0 is not considered
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

##################
# Main() to test #
##################
if __name__ == '__main__':
    bh = BinHeap()
    bh.buildHeap([9,5,6,2,3])
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())

