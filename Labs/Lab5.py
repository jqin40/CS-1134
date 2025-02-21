#TODO: from 1e to the end
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        elif ind < 0:
            ind = self.n+ind
        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        elif ind < 0:
            ind = self.n+ind
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        result = '['
        for i in range(self.n):
            result += f'{self[i]}, '
        result = result[:-2] + ']' #cut off last comma and space, put bracket
        return result

    def __add__(self, other):
        result = ArrayList()
        for elem in self:
            result.append(elem)
        for elem in other:
            result.append(elem)
        return result

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self

def main():
    arr1 = ArrayList()
    arr1.append(1)
    arr1.append(2)
    arr1.append(3)
    arr2 = ArrayList()
    arr2.append(4)
    arr2.append(5)
    arr2.append(6)
    print(arr1)

    # print(arr1 + arr2)

    # arr1 += arr2
    # print(arr1)

    # print(arr1[-1])
    # arr1[-1] = 5
    # print(arr1[-1])
main()

