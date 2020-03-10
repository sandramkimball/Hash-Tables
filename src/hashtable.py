# HASHING - provides O(1) time on average for insert, serach, delete
# SEPERATE CHAINING - each hash table cell points to list of same hashed values (a side road)

# Mon: Implement insert, remove, retrieve
# Tues: Linked lists to avoid collisions

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

    # _underscore = don't touch, don't use outside class, is private
    def _hash(self, key):
       # Hash an arbitrary key and return an integer.
        return hash(key)


    def _hash_djb2(self, key):
        #k=33 (33 magically works better somehow)
        return hash(key) = hash(key-1) * 33 ^ str[key]
        

    def _hash_mod(self, key): # creates/finds index?
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value): # key=index / O(1)
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            print('Error: key is use')
        else: 
            self.storage[key] = value


    def remove(self, key): # O(1)
        index = self._hash_mod(key)

        if self.storage[index] is not None:
             self.storage[index] = None
        else: 
            print('Key not found')


    def retrieve(self, key):
        index = self._hash_mod(key)
        return self.storage[index]


    def resize(self):
        # need to rehash everything into new index else nums change and won't be able to find anything(?)
        self.capacity *= 2
        new_storage = [None] * self.capacity
        old_storage = self.storage.copy()

        for bucket_item in old_storage:
            self.insert(bucket_item.key, bucket_item.value)




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
