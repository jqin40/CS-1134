from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue
from DoublyLinkedList import DoublyLinkedList
#Practice Exam
#4.
def alternating_parity(lst):
    q = ArrayQueue() #holds events
    s = ArrayStack() #holds odds
    for elem in lst:
        if elem % 2 == 0:
            q.enqueue(elem)
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 2 == 1:
            s.push(lst[i])
    for i in range(len(lst)):
        if i % 2 == 0:
            lst[i] = q.dequeue()
        else:
            lst[i] = s.pop()

# lst = [2, 8, 1, 7, 3, 4]
# alternating_parity(lst)
# print(lst) #[2, 1, 8, 7, 4, 3]

#5.
class FlippableStack:
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.flipped = False
    def __len__(self):
        return len(self.dll)
    def is_empty(self):
        return len(self) == 0
    def push(self, item):
        if not self.flipped:
            self.dll.add_last(item)
        else:
            self.dll.add_first(item)
    def pop(self):
        if (self.is_empty()):
            raise Exception("FlippableStack is empty")
        elif not self.flipped:
            return self.dll.delete_last()
        else: #flipped
            return self.dll.delete_first()
    def top(self):
        if (self.is_empty()):
            raise Exception("FlippableStack is empty")
        elif not self.flipped:
            return self.dll.trailer.prev.data
        else: #flppped
            return self.dll.header.next.data
    def flip(self):
        self.flipped = not self.flipped

# fs = FlippableStack()
# fs.push(1)
# fs.push(2)
# fs.push(3)
# fs.push(4)
# fs.push(5)
# fs.pop()
# fs.pop()
# print(fs.dll)
# fs.flip()
# fs.pop()
# fs.push(6)
# print(fs.dll)
# fs.pop()
# fs.pop()
# fs.pop()
# print(fs.dll)
