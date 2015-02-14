#################################################################################
#                         Binary Tree                                           #
# The root value, as well as the left and right subtrees                        #
#################################################################################

class BinaryTree:
    def __init__(self,rootObj):
        """creates a new instance of a binary tree of root rootObj"""
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        """creates a new binary tree and installs it as the left child of the current node"""
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            # insert a node and push the existing child down one level in the tree
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        """creates a new binary tree and installs it as the right child of the current node"""
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            # insert the node between the root and an existing right child
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """returns the binary tree corresponding to the right child of the current node"""
        return self.rightChild

    def getLeftChild(self):
        """returns the binary tree corresponding to the left child of the current node"""
        return self.leftChild

    def setRootVal(self,obj):
        """stores the object in parameter val in the current node"""
        self.key = obj

    def getRootVal(self):
        """returns the object stored in the current node"""
        return self.key

    def getMinDepth(self):
        """returns the min depth of this binary tree (it means the root)"""
        return 1 + min(self.leftChild.getMinDepth(), self.leftChild.getMinDepth()) if self.key != null else 0

    def getMaxDepth(self):
        """returns the Max depth of this binary tree (it means the root)"""
        return 1 + max(self.leftChild.getMaxDepth(), self.leftChild.getMaxDepth()) if self.key != null else 0

    def inOrder(self):
        """in Order"""
        if self.key:
            if self.leftChild:
                self.leftChild.inOrder()
            print(self.key)
            if self.rightChild:
                self.rightChild.inOrder()
