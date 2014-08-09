#################################################################################
#                         Selection Sort                                        #
# looks for the largest value as it makes a pass and, after completing the pass #
# places it in the proper location                                              #
#################################################################################

def selectionSort(alist):
    """On each pass, the largest remaining item is selected and then placed in its proper location"""
    for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location] > alist[positionOfMax]:
               positionOfMax = location
       alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


##################
# Main() to test #
##################
if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    selectionSort(alist)
    print(alist)
