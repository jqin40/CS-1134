from ArrayStack import *

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.maximum = None

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def push(self, e):
        if self.is_empty():
            self.maximum = e
        else:
            if e > self.maximum:
                self.maximum = e
        #second number of tuple represents max of everything up to and including this element
        self.data.push((e, self.maximum))

    def top(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        temp = self.data.pop()[0]
        if not self.is_empty():
            self.maximum = self.data.top()[1]
        else: #no elements left in stack, set max to None
            self.maximum = None
        return temp

    def max(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.top()[1]

#comment out when done
# def main():
#     maxS = MaxStack()
#     maxS.push(3) # 3 3
#     maxS.push(1) # 1 3
#     maxS.push(6) # 6 6
#     maxS.push(4) # 4 6
#     print(len(maxS)) #4
#     print(maxS.max()) #6
#     print(maxS.pop()) #4
#     print(maxS.pop()) #6
#     print(maxS.max()) #3
#     maxS.push(2) # 2 3
#     print(maxS.max()) # 3
#     print(maxS.top()) # 2
#     maxS.push(7) # 7 7
#     print(maxS.max()) # 7
#     print(maxS.top()) # 7
#     print(maxS.pop()) # 7
#
#     maxS2 = MaxStack()
#     maxS2.push(7)  # 7 7
#     maxS2.pop()  # 7
#     maxS2.push(1)  # should be 1 1
#     print(maxS2.max())  # 1
#     print(maxS2.top())  # 1
#
# main()