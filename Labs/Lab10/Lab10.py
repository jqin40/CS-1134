from DoublyLinkedList import DoublyLinkedList
#1
class LinkedStack:
    def __init__(self):
        self.dll = DoublyLinkedList()
    def __len__(self):
        return len(self.dll)
    def is_empty(self):
        return len(self.dll) == 0
    def push(self, e):
        self.dll.add_last(e)
    def top(self):
        if self.is_empty():
            raise Exception("LinkedStack is empty")
        return self.dll.trailer.prev
    def pop(self):
        if self.is_empty():
            raise Exception("LinkedStack is empty")
        return self.dll.delete_last()

# ls = LinkedStack()
# ls.push(1)
# print(ls.pop())

#Question 2 is in the DLL file

#3.
class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = None #refers to the Node at the middle, NOT the index

    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def push(self, e):
        self.data.add_last(e)
        if len(self.data) == 1:
            self.mid = self.data.header.next
        elif len(self.data) % 2 == 1:
            self.mid = self.mid.next

    def top(self):
        if self.data.is_empty():
            raise Exception("MidStack is empty")
        return self.data.trailer.prev
    def pop(self):
        if self.data.is_empty():
            raise Exception("MidStack is empty")
        temp = self.data.delete_last()
        if self.data.is_empty():
            self.mid = None
        elif len(self.data) % 2 == 0:
            self.mid = self.mid.prev
        return temp

    def mid_push(self, e):
        if self.data.is_empty():
            raise Exception("MidStack is empty")
        self.data.add_after(self.mid, e)
        if len(self.data) % 2 == 1:
            self.mid = self.mid.next

# def main3():
#     ms = MidStack()
#     print(ms.mid) #None
#     ms.push(0)
#     print(ms.mid.data) # 0
#     ms.push(1)
#     print(ms.mid.data) # 0
#     ms.push(2)
#     print(ms.mid.data) # 1
#     ms.push(3)
#     print(ms.mid.data) # 1
#     ms.push(4)
#     print(ms.mid.data) # 2
#     ms.push(5)
#     print(ms.mid.data) # 2
#     ms.pop() # 0 1 2 3 4
#     ms.mid_push(7) # 0 1 2 7 3 4
#     print(ms.mid.data) #2
#     ms.mid_push(8) # 0 1 2 8 7 3 4
#     print(ms.mid.data) #8
#
# main3()

#4.
def reverse_dll_by_data(dll):
    left_node = dll.header.next
    right_node = dll.trailer.prev
    while left_node is not right_node and left_node.prev is not right_node:
        left_node.data, right_node.data = right_node.data, left_node.data
        left_node = left_node.next
        right_node = right_node.prev

#TODO:doesn't work
def reverse_dll_by_node(dll):
    left_node = dll.header.next
    right_node = dll.trailer.prev
    while left_node is not right_node and left_node.prev is not right_node:
        #swap the two nodes
        temp_left = left_node
        left_node.next = right_node.next
        left_node.prev = right_node.prev
        right_node.next = temp_left.next
        right_node.prev = temp_left.prev
        #increment pointers
        left_node = left_node.next
        right_node = right_node.prev


def main4():
    dll = DoublyLinkedList()
    dll.add_last(0)
    dll.add_last(1)
    # dll.add_last(2)
    # dll.add_last(3)
    reverse_dll_by_node(dll)
    print(dll)

main4()