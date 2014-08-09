#################################################################################
#                         MAP                                                   #
# an unordered collection of associations between a key and a data value        #
# The keys in a map are all unique so that there is a one-to-one relationship   #
# between a key and a value                                                     #
#################################################################################

class HashTable(object):
    """Abstract Data Type"""
    def __init__(self, size=11):
        """list, called slots, will hold the key items and a parallel list, called data, will hold the data values. Size be a prime number"""
        # prime nb so that the collision resolution algorithm can be as efficient as possible
        self.size = size
        # the key list as a hash table
        self.slots = [None] * self.size
        # we look up a key, the corresponding position in the data list will hold the associated data value
        self.data = [None] * self.size

    def hashfunction(self,key,size):
        """simple remainder method module size"""
        return (key % size)

    def rehash(self,oldhash,size):
        """linear probing with a 'plus 1' rehash function"""
        return ((oldhash + 1) % size)

    def put(self,key,data):
        """Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value"""
        # assumes that there will eventually be an empty slot unless the key is already present 
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None:
            # empty slot
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] == key:
            # key is already in the map
            self.data[hashvalue] = data
        else:
            # linear probing for collision resolution
            nextslot = self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))
            if self.slots[nextslot] == None:
                # empty slot
                self.slots[nextslot]=key
                self.data[nextslot]=data
            else:
                # key is already in the map
                self.data[nextslot] = data
                
    def get(self,key):
        """Given a key, return the value stored in the map or None otherwise"""
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    # will terminate by checking to make sure that we have not returned to the initial slot
                    stop = True
        return data

    def delete(self,key):
        """Delete the key-value pair from the map"""
        position = self.hashfunction(key,len(self.slots))
        self.slots[position] == None
        self.data[position] == None

    def contains(self, key):
        """True for a statement of the form key in map"""
        return (key in self.slots)

    def length(self):
        """the number of key-value pairs stored in the map"""
        return len(self.slots)

    def __getitem__(self,key):
        """to implement evaluation of self[key]"""
        return self.get(key)

    def __setitem__(self,key,data):
        """to implement assignment to self[key]=data"""
        self.put(key,data)

    def __delitem__(self,key):
        """to implement deletion of self[key] as del self[key]"""
        self.delete(key)

    def __len__(self):
        """return the length as len(self)"""
        return self.length()

    def __contains__(self, key):
        """ to implement membership test operators as key in self"""
        self.contains(key)


##################
# Main() to test #
##################
if __name__ == '__main__':
    H=HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.slots)
    print(H.data)
    print(str(len(H)))
    print(17 in H)
    del H[20]
    H[20]='duck'
    print (H[20])
