#################################################################################
#                          Binary Search Tree                                   #
# keys that are less than the parent are found in the left subtree              #
# keys that are greater than the parent are found in the right subtree          #
#################################################################################

class BinarySearchTree:
    """Binary Seach Tree with reference to the root TreeNode object"""
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def _put(self,key,val,currentNode):
        """recursive insertion of key in binary search tree of root currentNode"""
        if key < currentNode.key:
            # key should be left under the current node
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            # key should be right under the current node
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def _get(self,key,currentNode):
        """recursive search of key until reaching a leaf. Returns the TreeNode or None"""
        if not currentNode:
            """leaf, key is not present"""
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def put(self,key,val):
        """insert the key/val in tree according to the binary search tree property"""
        if self.root:
            # recursive insertion from root node
            self._put(key,val,self.root)
        else:
            # new node becomes the root
            self.root = TreeNode(key,val)
        self.size = self.size + 1


    def get(self,key):
        """returns the payload of matching key or None"""
        if self.root:
            res = self._get(key,self.root)
        if res:
            return res.payload
        else:
            # no root Node, the tree is empty
            return None

    def remove(self,currentNode):
        """remove the current node in binary search tree"""
        if currentNode.isLeaf():
            #leaf, update its parent left child or right child
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            # interior node with left and right children
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            # replace key,payload of deleted node by those of successor
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            # this node has only one child either left or right
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    # node to be deleted is the root to be replaced by left child
                    currentNode.replaceNodeData(currentNode.leftChild.key,currentNode.leftChild.payload,currentNode.leftChild.leftChild,currentNode.leftChild.rightChild)
            else:
                # node has only right child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    # node to be deleted is the root to be replaced by right child
                    currentNode.replaceNodeData(currentNode.rightChild.key,currentNode.rightChild.payload,currentNode.rightChild.leftChild,currentNode.rightChild.rightChild)

    def delete(self,key):
        """the deletion of a key or raise an error"""
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                # remove keeping the binary search tree property
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif (self.size == 1 and self.root.key == key):
            # root is deleted
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __setitem__(self,k,v):
        """overload the [] operator for assignment"""
        self.put(k,v)
        
    def __getitem__(self,key):
        """return yourTree[key]"""
        return self.get(key)

    def __contains__(self,key):
        """overload the in operator"""
        return(self._get(key,self.root) != None)

    def __delitem__(self,key):
        """overload the del operator"""
        self.delete(key)
    
    def __len__(self):
        """overload the len operator"""
        return self.size

    def __iter__(self):
        return self.root.__iter__()


class TreeNode:
    """node with key,payload and optionally left/right children and parent nodes"""
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        """returns left child or None"""
        return self.leftChild

    def hasRightChild(self):
        """returns right child or None"""
        return self.rightChild

    def isLeftChild(self):
        """returns True if node is the left child of its parent if any"""
        return (self.parent and self.parent.leftChild == self)

    def isRightChild(self):
        """returns True if node is the right child of its parent if any"""
        return (self.parent and self.parent.rightChild == self)

    def isRoot(self):
        """returns True if no parent"""
        return not self.parent

    def isLeaf(self):
        """returns True if node has no children"""
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        """returns True if node has at least one child"""
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """return True if node has both left and right children"""
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        """replace node with thoses arguments"""
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        # self is now parent of lc and rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findMin(self):
        """return the TreeNode with minimum key value on tree rooted on that node"""
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findSuccessor(self):
        """find TreeNode with the smallest key > key of this node in the tree rooted on that node"""
        succ = None
        if self.hasRightChild():
            # the successor is the smallest key in the right subtree
            succ = self.rightChild.findMin()
        elif self.parent:
            # node has a parent but no right children
            if self.isLeftChild():
                # successor is the parent
                succ = self.parent
            else:
                # node is the only right child of its parent, successor is the successor of its parent, excluding this node
                self.parent.rightChild = None
                succ = self.parent.findSuccessor()
                self.parent.rightChild = self
        return succ

    def spliceOut(self): 
        """this node to be spliced out, has either left children or right children but not both"""
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            # self has either left children or right children
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __iter__(self):
        """overload for in ..."""
        if self:
            if self.hasLeftChild():
                # recursive call to __iter__() through for in...
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                # recursive call to __iter__() through for in...
                for elem in self.rightChild:
                    yield elem



##################
# Main() to test #
##################
if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    mytree[5]="green"
    for i in mytree:
        print(i, mytree[i])
    mytree.delete(5)
    for i in mytree:
        print(i, mytree[i])
    
    

