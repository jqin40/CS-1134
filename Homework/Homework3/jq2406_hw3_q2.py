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

    def insert(self, index, val):
        if index < 0: index += self.n
        if not (0 <= index < self.n):
            raise IndexError('invalid index')
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.append(val)
        i = self.n-1
        while i > index:
            self[i], self[i-1] = self[i-1], self[i]
            i -= 1

    def pop(self, index=None):
        if self.n == 0: raise IndexError("empty list")
        if index is None: index = self.n - 1
        elif index < 0: index += self.n
        if not (0 <= index < self.n): raise IndexError("invalid index")
        temp = self[index]

        #move the indexed element to the end if it's not there already
        while index < self.n-1:
            self[index], self[index+1] = self[index+1], self[index]
            index += 1

        #now remove the element at the end by decreasing the size
        self.n -= 1
        if self.n < self.capacity // 4:
            self.capacity //= 2
        return temp

# def main():
    #test for a
    # arr_lst = ArrayList()
    # for i in range(1, 4+1):
    #     arr_lst.append(i)
    # arr_lst.insert(-1, 30)
    # print(arr_lst)
    #
    # test for b/d
    # arr_lst = ArrayList()
    # for i in range(1, 5+1):
    #     arr_lst.append(i)
    # print(arr_lst.pop(-5)) #1
    # print(arr_lst.pop()) #5
    # print(arr_lst.pop()) #4
    # print(arr_lst.pop()) #3
    # print(arr_lst)  #[2]
    # print(arr_lst.capacity) #4

# main()