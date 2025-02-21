from BinarySearchTreeMap import *

#part 2a
def create_chain_bst(n):
    """
    Takes a positive integer n, and returns a binary search tree with n
    nodes containing the keys 1, 2, 3, …, n. The structure of the tree should
    be one long chain of nodes leaning to the right
    """
    bst = BinarySearchTreeMap()
    for i in range(1, n+1):
        bst.insert(i, None)
    return bst

# def main2a():
#     bst = create_chain_bst(4)
#     for elem in bst:
#         print(elem, end=' ')# 1 2 3 4
#     print()
#
# main2a()

#part 2b
def create_complete_bst(n):
    """Receives a positive integer n, where n is of the form
    n=2k-1 for some non-negative integer k.
    Returns a binary search tree with n nodes, containing the keys
    1, 2, 3, …, n, structured as a complete binary tree."""
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    #base:
    if low == high:
        bst.insert(low, None)
    #recursive case
    else:
        mid = (low+high)//2
        bst.insert(mid, None)
        add_items(bst, low, mid-1)
        add_items(bst, mid+1, high)

# def main2b():
#     bst = create_complete_bst(7)
#     for elem in bst:
#         print(elem, end=' ') #1 2 3 4 5 6 7
#     print()
#
#     bst = create_complete_bst(15)
#     for elem in bst:
#         print(elem, end=' ') #numbers 1-15
#     print()
#
# main2b()

# #Check q1
# bst = BinartSearchTreeMap()
# bst.insert(9, None)
# bst.insert(7, None)
# bst.insert(13, None)
# bst.insert(3, None)
# bst.insert(11, None)
# bst.insert(15, None)
# bst.insert(1, None)
# bst.insert(5, None)
#
# for elem in bst:
#     print(elem, end=' ') #1 3 5 7 9 11 13 15
# print()
#
# bst[6] = None
# bst[12] = None
# bst[4] = None
# bst[14] = None
# del bst[7]
# del bst[9]
# del bst[13]
# del bst[1]
# del bst[3]
#
# for elem in bst:
#     print(elem, end=' ') #4 5 6 11 12 14 15
# print()