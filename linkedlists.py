#################################################################################
#                         Linked Lists                                          #
# The list class itself does not contain any node objects                       #
# Instead it contains a single reference to only the first node                 #
#################################################################################

class Node:
    def __init__(self,initdata):
        """First, the node must contain the list item itself. We will call this the data field of the node. In addition, each node must hold a reference to the next node (None by default)"""
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext



class UnorderedList:

    def __init__(self):
        """list object will maintain a single reference to the head of the list"""
        self.head = None
        #self.tail = None

    def isEmpty(self):
        """to see whether the list is empty. It needs no parameters and returns a boolean value"""
        return self.head == None

    def add(self,item):
        """adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list"""
        temp = Node(item)
        temp.setNext(self.head)
##        if self.head == None:
##            self.tail = temp
        self.head = temp


##    def append(self,item):
##        """adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list"""
##        temp = Node(item)
##        if self.tail != None:
##            self.tail.setNext(temp)
##        self.tail = temp
##        if self.head == None:
##            self.head = temp

    def size(self):
        """returns the number of items in the list. It needs no parameters and returns an integer"""
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        """searches for the item in the list. It needs the item and returns a boolean value"""
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        """removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list"""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # we assume item is present
        if previous == None:
            # the item to be removed happens to be the first item
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())



class OrderedList(UnorderedList):
    def __init__(self):
        UnorderedList.__init(self)

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

            
