#############################################################################################
#                         Hashing                                                           #
# A hash table is a collection of items which are stored in such a way as                   #
# to make it easy to find them later. Each position of the hash table, often called a slot, #
# can hold an item and is named by an integer value starting at 0                           #
#############################################################################################

def hash(astring, tablesize):
    """ordinal values, add them up, and use the remainder method to get a hash value""" 
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) * (pos+1)
    return (sum % tablesize)


##################
# Main() to test #
##################
if __name__ == '__main__':
    print (hash("cat", 11))
