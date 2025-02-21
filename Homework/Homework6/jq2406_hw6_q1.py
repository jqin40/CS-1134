from DoublyLinkedList import *

class LinkedQueue:
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        new_node = DoublyLinkedList.Node(e)
        self.dll.trailer.prev.next = new_node
        new_node.prev = self.dll.trailer.prev
        new_node.next = self.dll.trailer
        self.dll.trailer.prev = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty")
        temp = self.dll.header.next.data
        self.size -= 1

        self.dll.header.next = self.dll.header.next.next
        self.dll.header.next.prev.disconnect() #disconnect the node after the header
        self.dll.header.next.prev = self.dll.header
        return temp

    def first(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty")
        return self.dll.header.next.data

# def main():
#     q = LinkedQueue()
#     print(q.is_empty()) #True
#     q.enqueue(1)
#     q.enqueue(2)
#     q.enqueue(3)
#     print(q.size) #3
#     print(q.dll)
#     print(q.dequeue()) #1
#     q.dequeue()
#     q.dequeue()
#     print(q.dll)
#     print(q.is_empty()) #True
#     q.enqueue(5)
#
# main()