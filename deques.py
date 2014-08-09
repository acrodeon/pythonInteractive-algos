#################################################################################
#                         Deques                                                #
# A double-ended queue, is an ordered collection of items similar to the queue  #
# New items can be added at either the front or the rear                        #
# Likewise, existing items can be removed from either end                       #
# The rear of the deque is at position 0 in the list                            #
# adding and removing items from the front is O(1)                              #
# whereas adding and removing from the rear is O(n)                             #
#################################################################################

class Deque:
    def __init__(self):
        """creates a new deque that is empty. It needs no parameters and returns an empty deque"""
        self.items = []

    def isEmpty(self):
        """to see whether the deque is empty. It needs no parameters and returns a boolean value"""
        return self.items == []

    def addFront(self, item):
        """adds a new item to the front of the deque. It needs the item and returns nothing"""
        self.items.append(item)

    def addRear(self, item):
        """adds a new item to the rear of the deque. It needs the item and returns nothing"""
        self.items.insert(0,item)

    def removeFront(self):
        """removes the front item from the deque. It needs no parameters and returns the item. The deque is modified"""
        return self.items.pop()

    def removeRear(self):
        """removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified"""
        return self.items.pop(0)

    def size(self):
        """returns the number of items in the deque. It needs no parameters and returns an integer"""
        return len(self.items)

##################
# Main() to test #
##################
if __name__ == '__main__':

    def palchecker(aString):
        chardeque = Deque()

        for ch in aString:
            chardeque.addRear(ch)

        stillEqual = True
        while chardeque.size() > 1 and stillEqual:
            first = chardeque.removeFront()
            last = chardeque.removeRear()
            if first != last:
                stillEqual = False

        return stillEqual

    print(palchecker("lsdkjfskf"))
    print(palchecker("radar"))
