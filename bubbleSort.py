#################################################################################
#                         Bubble Sort                                           #
# It compares adjacent items and exchanges those that are out of order          #
# Each pass through the list places the next largest value in its proper place  #
#################################################################################

def bubbleSort(alist):
    """each item “bubbles” up to the location where it belongs"""
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                
def shortBubbleSort(alist):
    """a bubble sort may have an advantage in that it will recognize the sorted list and stop"""
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i] > alist[i+1]:
               exchanges = True
               alist[i], alist[i+1] = alist[i+1], alist[i]
       passnum = passnum-1

##################
# Main() to test #
##################
if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    bubbleSort(alist)
    print(alist)
    alist=[20,30,40,90,50,60,70,80,100,110]
    shortBubbleSort(alist)
    print(alist)
