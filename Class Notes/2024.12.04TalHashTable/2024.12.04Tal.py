# from lists import ArrayList
from lists import array
import random

class LinearFunction:
    def __init__(self, m, b):
        self.m = m
        self.b = b

    #special method call
    def __call__(self, x):
        return self.m * x + self.b

# g1 = LinearFunction(2, 5)
# g2 = LinearFunction(3, -3)
# print(g1(7)) #19

# class MAD_HashFunction:
#     def __init__(self, N, p=40205835204840513073):
#         self.N = N
#         self.p = p
#         self.a = random.randint(1, self.p-1) #closed interval; b is included
#         self.b = random.randint(0, self.p-1)
#
#     def __call__(self, key):
#         return ((self.a * hash(key) + self.b) % self.p) % self.N
#
# h = MAD_HashFunction(10)
#call h with a key and get a number between 0 and 9

class UnsortedArrayMap():
    def Item(...):
        ...

    def __getitem__(self, item):
        for item in self.table:
            if(item.key == key):
                ...
    def __setitem__(self, key, value):
        for item in self.table:
            if (item.key == key):
                item.value = value
                return
        new_item = UnsortedArrayMap.Item(key, value)
        self.table.append(new_item)

class ChainingHashTableMap:
    class MAD_HashFunction:
        def __init__(self, N, p=40205835204840513073):
            self.N = N
            self.p = p
            self.a = random.randint(1, self.p - 1)  # closed interval; b is included
            self.b = random.randint(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N

    def __init__(self, N=32):
        self.N = N #size of table
        self.table = make_array(self.N)
        for i in range(self.N):
            self.table[i] = UnsortedArrayMap()
        self.n = 0 #entries filled
        self.h = ChainingHashTableMap.MAD_HashFunction(self.N)

    def __len__(self):
        pass

    def is_empty(self):
        pass

    def __getitem__(self, key):
        #run the hash function on the key
        i = self.h(key)
        curr_bucket = self.table[i] #curr bucket is an unsorted array map
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.h(key)
        curr_bucket = self.table[i] #curr bucket is an unsorted array map
        old_size = len(curr_bucket)
        curr_bucket[key] = value # curr_bucket.__setitem__(key,value)
        new_size = len(curr_bucket)
        if new_size > old_size:
            self.n += 1
        if self.n > self.N:
            self.rehash(2 * self.N) #resize

    def __delitem__(self, key):
        # run the hash function on the key
        i = self.h(key)
        curr_bucket = self.table[i]  # curr bucket is an unsorted array map, secondary collection
        del curr_bucket[key] #uses delitem method from unsorted array map
        self.n -= 1
        if (self.n < (self.N // 4)):
            self.rehash(self.N // 2)

    def rehash(self, new_size):
        old_data = [(key, self[key]) for key in self] #list of key value pairs
        self.__init__(new_size)
        for (key, value) in  old_data:
            self[key] = value
        #what does key value pair represent?

    def __iter__(self):
        for i in range(self.N):
            curr_bucket = self.table[i]
            for key in curr_bucket:
                yield key

    def __contains__(self, key):
        try:
            value = self[key]
            return True
        except KeyError:
            return False
