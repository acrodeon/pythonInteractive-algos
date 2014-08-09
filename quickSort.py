#################################################################################
#                         Quick Sort                                            #
# A quick sort first selects a value, which is called the pivot value           #
# The actual position where the pivot value belongs in the final sorted list,   #
# the split point, will be used to divide the list for subsequent calls         #
#################################################################################

def quickSort(alist):
    """Quick Sort of alist"""
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    """quick sort from first to last (included)"""
    # first == last, list of one element is already sorted
    print(alist, first, last)
    if first < last:
        # pivot is at splitpoint in the final sorted list
        splitpoint = partition(alist,first,last)
        print(splitpoint, alist)
        # index < splitpoint => alist[index] <= pivot
        quickSortHelper(alist,first,splitpoint-1)
        # index > splitpoint => alist[index] > pivot
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    """pivot at first position"""
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        # leftmark is going to be the first left value > pivotvalue
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
        # rightmark is going to be the first right value < pivotvalue
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
        # rightmark < leftmark => splitpoint has been found
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    # at splitpoint, pivotvalue goes to its final position
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark
 



##################
# Main() to test #
##################
if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist)
