#################################################################################
#                          Balanced Binary Search Tree                          #
# keys that are less than the parent are found in the left subtree              #
# keys that are greater than the parent are found in the right subtree          #
# balanceFactor=height(leftSubTree)−height(rightSubTree) = -1, 0 or 1           #
#################################################################################

from binarySearchTree import BinarySearchTree, TreeNode

class AVLTree(BinarySearchTree):
    """Binary Seach Tree with reference to the root TreeNode object"""
    def __init__(self):
        BinarySearchTree.__init__(self)

    def rotateLeft(self,rotRoot):
        """Promote the right child to be the root of the subtree.Move the old root to be the left child of the new root. If new root already had a left child then make it the right child of the new left child"""
        newRoot = rotRoot.rightChild
        # newRoot already had a left child then make it the right child of rotRoot
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            # if rotRoot was the root of the AVLTree 
            self.root = newRoot
        # parent of rotRoot to be parent of newRoot
        elif rotRoot.isLeftChild():
            rotRoot.parent.leftChild = newRoot
        else:
            rotRoot.parent.rightChild = newRoot
        # the old root to be the left child of the new root
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        # recompute balanceFactors
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot):
        """Promote the left child to be the root of the subtree.Move the old root to be the right child of the new root. If new root already had a right child then make it the left child of the new right child"""
        newRoot = rotRoot.leftChild
        # newRoot already had a right child then make it the left child of rotRoot
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            # if rotRoot was the root of the AVLTree 
            self.root = newRoot
        # parent of rotRoot to be parent of newRoot
        elif rotRoot.isLeftChild():
            rotRoot.parent.leftChild = newRoot
        else:
            rotRoot.parent.rightChild = newRoot
        # the old root to be the right child of the new root
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        # recompute balanceFactors
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)

    def rebalance(self,node):
        if node.balanceFactor < 0:
            # before rotateLeft on node, if right child if left heavy do a rotateRight
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            # before rotateRight on node, if left child if right heavy do a rotateLeft
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def updateBalance(self,node):
        """update blance factor of node with rotation if needed"""
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent:
            # node has balanceFactor=0, updates parent's balance
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                # update balance of parent to 0
                self.updateBalance(node.parent)

    def _put(self,key,val,currentNode):
        """override of put method to assure a good balance factor"""
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)

##################
# Main() to test #
##################
if __name__ == '__main__':
    mytree = AVLTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    mytree[5]="green"
    for i in mytree:
        print("key", i, "val", mytree[i], "balanceFactor", mytree._get(i,mytree.root).balanceFactor)
    
