from ArrayQueue import *

#1
class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.total = 0

    def __len__(self):
        # Return the number of elements in the queue
        return len(self.data)

    def is_empty(self):
        # Return True if queue is empty
        return len(self.data) == 0

    def enqueue(self, e):
        #Add element e to the end of the queue.
        # If e is not an int or float, raise a TypeError
        if type(e) == int or type(e) == float:
            self.data.enqueue(e)
            self.total += e
        else:
            raise TypeError("Not int or float")

    def dequeue(self):
        #Remove and return the first element from the queue.
        #If the queue is empty, raise an exception
        self.total -= e
        return self.data.dequeue()

    def first(self):
        """
        Return a reference to the first element of the queue without removing it.
        If the queue is empty, raise an exception
        """
        return self.data.first()
    def sum(self):
        #Returns the sum of all values in the queue
        return self.total
    def mean(self):
        #Return the mean(average) value in the queue
        return self.total / len(self.data)

#2
class ArrayDeque:
    INITIAL_CAPACITY = 8
    def __init__(self):
        #Initializes an empty Deque using an array as self.data
        self.data_arr = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.capacity = ArrayDeque.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None
        #Don't use back index, just calculate it on the fly when needed
        #back index: (front + n - 1) % n

    def __len__(self):
        #Return the number of elements in the Deque
        return self.n
    def is_empty(self):
        return self.n == 0
    def first(self):
        if (self.is_empty()):
            raise Exception("Deque is empty")
        return self.data_arr[self.front_ind]
    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.data_arr[(self.front_ind + self.n - 1) % self.n]

    #Add elem to the front of the ArrayDeque
    def enqueue_first(self, elem):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        if self.is_empty():
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else: #can enqueue an element
            self.front_ind = (self.front_ind - 1) % self.n
            self.data_arr[self.front_ind] = elem
            self.n += 1

    def enqueue_last(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = elem
            self.n += 1

    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Deque is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def dequeue_last(self):
        if (self.is_empty()):
            raise Exception("Deque is empty")
        back_ind = (self.front_ind + self.n - 1) % self.n
        value = self.data_arr[back_ind]
        self.data_arr[back_ind] = None
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    #resize copied from ArrayQueue, is this O(1) amortized?
    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0

    # def __repr__(self):
    #     for elem in self.data_arr:
    #         print(elem)

# def main():
    # d = ArrayDeque()
    # d.enqueue_first(1)
    # d.enqueue_first(2)
    # d.enqueue_first(3)
    # d.enqueue_first(4)
    # d.enqueue_first(5)
    # d.enqueue_first(6)
    # d.enqueue_first(7)
    # d.enqueue_first(8)

# main()

#3.
def flatten_list_by_depth(lst):
    """
    :lst type: list
    :return type: list
    """
    q = ArrayQueue()
    new_lst = []
    for elem in lst:
        q.enqueue(elem)
    ...
    return new_lst