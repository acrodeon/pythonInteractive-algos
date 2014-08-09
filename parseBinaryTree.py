#################################################################################
#                         Parse Binary Tree                                     #
# The BinaryTree provides us with a way to get children of a node               #
# To keeping track of parents as we traverse the tree is to use a stack         #
#################################################################################

from stack import Stack
from binaryTree import BinaryTree
import operator

def buildParseTree(fpexp):
    """build binary tree based on fexp"""
##    If the current token is a ')', go to the parent of the current node.
    # a list of the words in the string, using space as the delimiter 
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            # add a new node as the left child of the current node, and descend to the left child
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            # set the root value of the current node to the number and return to the parent
            currentTree.setRootVal(int(i))
            currentTree = pStack.pop()
        elif i in ['+', '-', '*', '/']:
            # set the root value of the current node to the operator represented by the current token
            # Add a new node as the right child of the current node and descend to the right child
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            # go to the parent of the current node
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    """to evaluate the parse tree, returning the numerical result"""
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        # apply operator to leftTree and rightTree
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        # a leaf here, ie a number as operand
        return parseTree.getRootVal()

def preorder(tree):
    """root, left, right"""
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    """left, right, root"""
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    """left, root, right"""
    if tree:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

def postordereval(tree):
    """evaluating the left subtree, evaluating the right subtree, and combining them in the root through the function call to an operator"""
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            # a leaf,ie a number as operand
            return tree.getRootVal()

def printexp(tree):
    """norder traversal of a parse tree we get our original expression back"""
    sVal = ""
    if tree:
        # print a left parenthesis before the recursive call to the left subtree
        if tree.getLeftChild():
            sVal = '('
        sVal += printexp(tree.getLeftChild())
        sVal += str(tree.getRootVal())
        # print a right parenthesis after the recursive call to the right subtree
        sVal += printexp(tree.getRightChild())
        if tree.getRightChild():
            sVal += ')'
    return sVal

##################
# Main() to test #
##################
if __name__ == '__main__':
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    print(evaluate(pt))
    print(postordereval(pt))
    preorder(pt)
    print()
    postorder(pt)
    print()
    inorder(pt)
    print()
    print(printexp(pt))
    

