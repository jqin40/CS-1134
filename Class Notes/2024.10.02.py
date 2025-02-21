import ctypes # provides low-level arrays

def make_array(n):
    #py_object is a datatype in C, refers to any object in Python
    return (n * ctypes.py_object)() #extra parentheses: creates an array of n ctypes.py_objects

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1) #inits the array with a capacity of 1
        self.capacity = 1 #initialize capacity
        self.n = 0 #number of elements in the array

    def __len__(self):
        return self.n

    def append(self, val):
        if self.n == self.capacity: #check if resizing is needed
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)    # create a new array of the new size
        for i in range(self.n):             # copy elements from old array to new
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array           # update reference to new array
        self.capacity = new_size            # update capacity

    def __getitem__(self, index):
        if not (0 <= index < self.n):
            raise IndexError('Invalid index')
        return self.data_arr[index]

    def __setitem__(self, index, val):
        if not (0 <= index < self.n):
            raise IndexError('Invalid index')
        self.data_arr[index] = val

    def extend(self, collection):
        for elem in collection:
            self.append(elem)

    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]

def main():
    array_list = ArrayList() #needs to be a constructor!

    array_list.append(10)
    print(id(array_list.data_arr))
    array_list.append(20)
    print(id(array_list.data_arr))
    array_list.append(30)
    print(id(array_list.data_arr))
    array_list.append(10)
    print(id(array_list.data_arr))
    array_list.append(20)
    print(id(array_list.data_arr))
    array_list.append(30)
    print(id(array_list.data_arr))

    print("Element at index 0:", array_list[0])
    print("Element at index 1:", array_list[1])
    # print("Element at index 0:", array_list[0])

main()