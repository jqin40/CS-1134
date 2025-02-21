from DoublyLinkedList import *

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(curr_node1, curr_node2, merge_dll):
        if curr_node1.data == None and curr_node2.data == None:
            return merge_dll
        elif curr_node1.data == None:
            #copy remaining nodes in second dll
            merge_dll.add_last(curr_node2.data)
            return merge_sublists(curr_node1, curr_node2.next, merge_dll)
        elif curr_node2.data == None:
            #copy remaining nodes in first dll
            merge_dll.add_last(curr_node1.data)
            return merge_sublists(curr_node1.next, curr_node2, merge_dll)
        elif curr_node1.data <= curr_node2.data:
            merge_dll.add_last(curr_node1.data)
            return merge_sublists(curr_node1.next, curr_node2, merge_dll)
        else: # curr_node1.data > curr_node2.data
            merge_dll.add_last(curr_node2.data)
            return merge_sublists(curr_node1, curr_node2.next, merge_dll)

    merge_dll = DoublyLinkedList()
    curr_node1 = srt_lnk_lst1.header.next
    curr_node2 = srt_lnk_lst2.header.next
    return merge_sublists(curr_node1, curr_node2, merge_dll)

# def main():
#     srt_lnk_lst1 = DoublyLinkedList()
#     srt_lnk_lst1.add_last(1)
#     srt_lnk_lst1.add_last(3)
#     srt_lnk_lst1.add_last(5)
#     srt_lnk_lst1.add_last(6)
#     srt_lnk_lst1.add_last(8)
#     print(srt_lnk_lst1)
#
#     srt_lnk_lst2 = DoublyLinkedList()
#     srt_lnk_lst2.add_last(2)
#     srt_lnk_lst2.add_last(3)
#     srt_lnk_lst2.add_last(5)
#     srt_lnk_lst2.add_last(10)
#     srt_lnk_lst2.add_last(15)
#     srt_lnk_lst2.add_last(18)
#     print(srt_lnk_lst2)
#
#     merge = merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2)
#     print(merge)
#
# main()