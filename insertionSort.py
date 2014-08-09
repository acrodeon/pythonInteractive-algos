#################################################################################
#                         Insertion Sort                                        #
# maintains a sorted sublist in the lower positions of the list                 #
# Each new item is then “inserted” back into the previous sublist such that     #
# the sorted sublist is one item larger                                         #
#################################################################################

def insertionSort(alist):
    """Insertion sort works at the start of the list. Each pass produces a longer sorted list"""
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue



##################
# Main() to test #
##################
if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    insertionSort(alist)
    print(alist)
