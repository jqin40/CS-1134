from ArrayStack import *
from ArrayDeque import *

class MidStack:
    def __init__(self):
        #use stack for the lower half, deque for the upper half
        self.stack = ArrayStack()
        self.deque = ArrayDeque()

    def is_empty(self):
        return (len(self.stack) + len(self.deque)) == 0

    def __len__(self):
        return len(self.stack) + len(self.deque)

    def push(self, e):
        self.deque.enqueue_last(e)
        #want the deque to always be < stack
        if len(self.deque) > len(self.stack):
            self.stack.push(self.deque.dequeue_first())

    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        elif not self.deque.is_empty():
            return self.deque.last()
        else: #deque is empty
            return self.stack.top()

    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        elif not self.deque.is_empty():
            return self.deque.dequeue_last()
        else:  # deque is empty
            return self.stack.pop()

    def mid_push(self, e):
        self.stack.push(e)
        #if deque is 2 smaller than deque,then move top of stack to front of deque
        #to balance out the stack and deque
        #(ensure the top of the stack remains mid)
        if len(self.deque) == len(self.stack)-2:
            self.deque.enqueue_first(self.stack.pop())

# def main1():
#     midS = MidStack()
#     midS.push(2)
#     midS.push(4)
#     midS.push(6)
#     midS.push(8)
#     midS.mid_push(10)
#     print(len(midS)) #5
#     print(midS.top()) #8
#     print(midS.pop()) # 8
#     print(midS.pop()) # 6
#     print(midS.pop()) # 10
#     print(midS.pop()) # 4
#     print(midS.pop()) # 2
#
# main1()

# def main2():
#     midS = MidStack()
#     midS.push(2)
#     midS.push(4)
#     midS.push(6)
#     midS.push(8)
#     midS.push(10)
#     midS.mid_push(12)
#     print(midS.pop()) # 10
#     print(midS.pop()) # 8
#     print(midS.pop()) # 12
#     print(midS.pop()) # 6
#     print(midS.pop()) # 4
#     print(midS.pop()) # 2
#
# main2()