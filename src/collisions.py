import random 

def how_many_before_collision(buckets, loops=1):
    #roll random hash indexes into bckts and prints how many rolls we can get

    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = str(random.random())
            hash_index = hash(random) % buckets #find index by: hash / mod
            if hash_index not in tried:
                tried.add(hash)
                tries += 1

            else:
                print('We have a Collision')
                break
        # .1f formats value for one decimal
        print(f'{buckets} buckets\n {tries} hashes.\n ({tries/buckets *100: .1f}%')
