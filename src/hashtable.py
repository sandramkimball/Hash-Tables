# HASHING - provides O(1) time on average for insert, serach, delete
# SEPERATE CHAINING - make each hash table cell point to a linked list of 
# records with same hash func value (a side road)

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.count = 0

class HashTable:
    '''
    A hash table with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
       # Hash an arbitrary key and return an integer.
        return hash(key)


    def _hash_djb2(self, key):
        #k=33 (33 magically works better somehow)
        return hash(key) = hash(key-1) * 33 ^ str[key]
        


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value): # key=index / O(1)
        if self.count >= self.capacity:
            self.resize()
        if key > self.count:
            print('Error: out of range')
            return
        
        for i in range(count, key, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[key] = value
        self.count += 1


    def remove(self, key): # O(1)
        for i in range(self.count, key, -1):
            if self.storage.retrieve(key):
                key.pop()
                self.count -= 1


    def retrieve(self, key):
        if self.storage[key]:
            return key
        else:
            print('Error: key not found')
            return


    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range (self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
