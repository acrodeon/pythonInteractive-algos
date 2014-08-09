#################################################################################
#                         Queues                                                #
# an ordered collection of items which are added at one end, called the “rear,” #
# and removed from the other end, called the “front.”                           #
# the rear is at position 0 in the list.                                        #
# enqueue will be O(n) and dequeue will be O(1).                                #
#################################################################################

class Queue:
    def __init__(self):
        """creates a new queue that is empty. It needs no parameters and returns an empty queue"""
        self.items = []

    def isEmpty(self):
        """to see whether the queue is empty. It needs no parameters and returns a boolean value"""
        return self.items == []

    def enqueue(self, item):
        """adds a new item to the rear of the queue. It needs the item and returns nothing"""
        self.items.insert(0,item)

    def dequeue(self):
        """removes the front item from the queue. It needs no parameters and returns the item. The queue is modified"""
        return self.items.pop()

    def size(self):
        """returns the number of items in the queue. It needs no parameters and returns an integer"""
        return len(self.items)
