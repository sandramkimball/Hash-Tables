import hashlib
import sys
import json

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.count = 0

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
       # Hash an arbitrary key and return an integer.
        # return hashlib.sha256(key.encode())
        return hash(key)


    def _hash_djb2(self, key):
        #k=33 (33 magically works better somehow)
        return hash(key) == hash(key-1) * 33 ^ str[key]
        

    def _hash_mod(self, key): # creates/finds index?
        return self._hash(key) % self.capacity


    def insert(self, key, value): # key=index / O(1)
        index = self._hash_mod(key)

        # if self.storage[index] is not None:
        #     print('Error: key is use')
        # else: 
        #     self.storage[key] = value
        
        node = LinkedPair(key, value)
        node.next = self.storage[index]
        self.storage[index] = node


    def remove(self, key): # O(1)
        index = self._hash_mod(key)

        if self.storage[index] is None:
             return

        head = self.storage[index]
        if self.storage[index]:
            self.storage[index] = head.next
            return

        bucket = self.storage[index]
        previous = head
        while bucket:
            if bucket.key == key:
                previous.next = bucket.next
                return
            else:
                previous = bucket
                bucket = bucket.next


    def retrieve(self, key):
        index = self._hash_mod(key)
        head = self.storage[index]

        while head:
            if head.key == key:
                return head.value
            head = head.next

        return None


    def resize(self):
        # need to rehash everything into new index else nums change and won't be able to find anything(?)
        new_storage = [None] * self.capacity * 2
        old_storage = self.storage
        self.storage = new_storage
        self.capacity *= 2


        for bucket_item in old_storage:
            while bucket_item:
                self.insert(bucket_item.key, bucket_item.value)
                bucket_item = bucket_item.next

        # self.capacity = int(self.capacity * 2)
        # temp_hashtable = HashTable(self.capacity)
        # new_storage = [None] * self.capacity * 2


        # for node in self.storage:
        #     while node:
        #         new_storage.insert(node.key, node.value)
        #         node = node.next

        self.storage = new_storage

    def shrinksize(self):
        self.capacity = self.capacity / 2
        new_storage = [None] * self.capacity
        old_storage = self.storage.copy()

        for bucket_item in old_storage:
            self.insert(bucker_item.key, bucket_item.value)


    #linkedlist to handle collisions...how tf to integrate?
    def linked_list(keys, buckets, loops=10):
        #O(n) time for Linked List
        #roll keys num of keys into bckts num of random bckts and count collisions

        for i in range(loops):
            key_counts = {} #empty dictionary
            for i in range(buckets):
                key_counts[i] = 0
            for i in range(keys):
                random_key = str(random.random())
                hash_index = hash(random_key) % buckets
                key_counts[hash_index] += 1

            largest_n = 0
            for key in key_counts:
                if key_counts[key] > largest_n:
                    largest_n = key_counts[key]


    #def auto-resize(self):
        # if load-factor > .07:
        #     resize()
        # if load factor < .02:
        #     halfsize()


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
