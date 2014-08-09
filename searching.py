#################################################################################
#                         Searching                                             #
# the algorithmic process of finding a particular item in a collection of items #
# A search typically answers either True or False                               #
#################################################################################

def sequentialSearch(alist, item):
    """index values are ordered, it is possible for us to visit them in sequence"""
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

def orderedSequentialSearch(alist, item):
    """the list of items was constructed so that the items were in ascending order"""
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos = pos+1
    return found

def binarySearch(alist, item):
    """If the item we are searching for is greater than the middle item, we know that the entire lower half of the list as well as the middle item can be eliminated from further consideration"""
    first = 0
    last = len(alist)-1
    found = False
    # alist is ordered
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        elif item < alist[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
    return found

def recursiveBinarySearch(alist, item):
    """If the item we are searching for is greater than the middle item, we know that the entire lower half of the list as well as the middle item can be eliminated from further consideration"""
    if len(alist) == 0:
        return False
    else:
        # alist is ordered
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return recursiveBinarySearch(alist[:midpoint],item)
        else:
            return recursiveBinarySearch(alist[midpoint+1:],item)




	
##################
# Main() to test #
##################
if __name__ == '__main__':
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(orderedSequentialSearch(testlist, 3))
    print(orderedSequentialSearch(testlist, 13))
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
    print(recursiveBinarySearch(testlist, 3))
    print(recursiveBinarySearch(testlist, 13))
