#################################################################################
#                         Shell Sort                                            #
# sort by breaking the original list into a number of smaller sublists,         #  
# each of which is sorted using an insertion sort                               #
# the shell sort uses an increment i, sometimes called the gap, to create       #
# a sublist by choosing all items that are i items apart                        #
#################################################################################

def shellSort(alist):
    """y sorting the sublists, we have moved the items closer to where they actually belong"""
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
            print("After increments of size",sublistcount,"The list is",alist)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    """sublists defined by gap are sorted with the basic insertion sort"""
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue


##################
# Main() to test #
##################
if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    shellSort(alist)
    print(alist)
