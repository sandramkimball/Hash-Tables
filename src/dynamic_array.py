
class DynamicArray:
    #usually arrays initializes with a size: my_array = [4](an array size of 4, not array containing 4)
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity #emulating allocating memory

    def insert(self, index, value): #index = location, place, address
        #first, check if: is there open space/index in range, shift things right, insert

        if self.count >= self.capacity:
            self.double_size()

        if index > self.count: #extra space gaps cause problemos
            print ('err: out of range')
            return
        
        #start with last, move right, iterate backwards:
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

# my_array = DynamicArray(4)
# my_array.insert(0, 1)
# my_array.insert(0, 2)
# my_array.insert(1, 3)
# my_array.insert(3, 4)
# my_array.insert(0, 5)
# print(my_array.storage)