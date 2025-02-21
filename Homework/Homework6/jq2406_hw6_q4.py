from DoublyLinkedList import *

def copy_linked_list(lnk_lst):
    '''given lnk_lst: a nested dll of integers and dlls
    return a shallow copy of lnk_lst'''
    result = DoublyLinkedList()
    curr_node = lnk_lst.header.next
    while curr_node.data is not None:
        result.add_last(curr_node.data)
        curr_node = curr_node.next
    return result

def deep_copy_linked_list(lnk_lst):
    result = DoublyLinkedList()
    curr_node = lnk_lst.header.next
    while curr_node.data is not None:
        if type(curr_node.data) == int:
            result.add_last(curr_node.data)
        else: #DLL
            dll_copy = deep_copy_linked_list(curr_node.data)
            result.add_last(dll_copy)
        curr_node = curr_node.next
    return result

# def main():
#     #shallow copy test
#     # lnk_lst1 = DoublyLinkedList()
#     # elem1 = DoublyLinkedList()
#     # elem1.add_last(1)
#     # elem1.add_last(2)
#     # lnk_lst1.add_last(elem1)
#     # elem2 = 3
#     # lnk_lst1.add_last(elem2)
#     #
#     # lnk_lst2 = copy_linked_list(lnk_lst1)
#     # e1 = lnk_lst1.header.next
#     # e1_1 = e1.data.header.next
#     # e1_1.data = 10
#     # e2 = lnk_lst2.header.next
#     # e2_1 = e2.data.header.next
#     # print(lnk_lst1)
#     # print(lnk_lst2)
#     # print(e2_1.data) #10
#
#     #deep copy test
#     lnk_lst1 = DoublyLinkedList()
#     elem1 = DoublyLinkedList()
#     elem1.add_last(1)
#     elem1_2 = DoublyLinkedList()
#     elem1_2.add_last(2)
#     elem1.add_last(elem1_2)
#     lnk_lst1.add_last(elem1)
#     elem2 = 3
#     lnk_lst1.add_last(elem2)
#
#     lnk_lst2 = deep_copy_linked_list(lnk_lst1)
#     e1 = lnk_lst1.header.next
#     e1_1 = e1.data.header.next
#     e1_1.data = 10
#     e1_2 = e1.data.header.next.next
#     e1_2.data = 20
#
#     e2 = lnk_lst2.header.next
#     e2_1 = e2.data.header.next
#     print(lnk_lst1)
#     print(lnk_lst2)
#     print(e2_1.data) #1
#
# main()