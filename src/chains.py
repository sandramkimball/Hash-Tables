import random

def longest_list_chain(keys, buckets, loops=10):
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

        print(f'Longest list for {keys} keys in {buckets} buckets\n (Load Factor: {keys/buckets:.2f})')