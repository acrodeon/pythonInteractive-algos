#################################################################################
#                         Merge Sort                                            #
# We split the list and recursively invoke a merge sort on both halves          #
# Once the two halves are sorted, the fundamental merge operation is performed  #
# Merging is the process of taking two smaller sorted lists and combining them  #
# together into a single, sorted, new list                                      #
#################################################################################

def mergeSort(alist):
    """Recursive Merge Sort"""
    print("Splitting ",alist)
    # the length of the list is less than or equal to one, then we already have a sorted list
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(alist, lefthalf, righthalf)

def merge(alist, lefthalf, righthalf):
    """Merge sorted left and right lists"""
    i=0
    j=0
    k=0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k] = lefthalf[i]
            i=i+1
        else:
            alist[k] = righthalf[j]
            j=j+1
            k=k+1

    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        alist[k] = righthalf[j]
        j=j+1
        k=k+1
    print("Merging ",alist)


##################
# Main() to test #
##################
if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    mergeSort(alist)
    print(alist)
