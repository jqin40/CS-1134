#TODO: __ makes __transfer a private method
from ArrayStack import *

class Queue:
    def __init__(self):
        #enq stack: enqueue stack
        #deq stack: dequeue stack
        #elements move from enq to deq in the method transfer
        self.enq = ArrayStack()
        self.deq = ArrayStack()

    def __len__(self):
        return len(self.enq) + len(self.deq)

    def is_empty(self):
        return (len(self.enq) + len(self.deq)) == 0

    def enqueue(self, e):
        self.enq.push(e)

    def __transfer(self):
        #transfers elements from the enq stack to the deq stack
        while not self.enq.is_empty():
            self.deq.push(self.enq.pop())

    def dequeue(self):
        if self.enq.is_empty() and self.deq.is_empty():
            raise Exception("Queue is empty")
        elif self.deq.is_empty():
            self.__transfer()
        return self.deq.pop()

    def first(self):
        if self.enq.is_empty() and self.deq.is_empty():
            raise Exception("Queue is empty")
        elif self.deq.is_empty():
            self.__transfer()
        return self.deq.top()

# def main():
#     q = Queue()
#     q.enqueue(1)
#     q.enqueue(2)
#     print(q.first()) # 1
#     q.enqueue(3)
#     q.enqueue(4)
#     print(q.dequeue()) # 1
#     print(q.dequeue()) # 2
#     print(q.first()) # 3
#     q.enqueue(5)
#     print(q.dequeue()) # 3
#     print(q.dequeue()) # 4
#     print(q.first()) # 5
#     print(q.dequeue()) # 5
#
# main()
