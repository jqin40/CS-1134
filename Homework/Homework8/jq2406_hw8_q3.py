from BinarySearchTreeMap import *

def restore_bst(prefix_lst):
    """
    Creates a binary tree that gives prefix_lst
    when scanned in prefix order
    """
    def make_node(val):
        item = BinarySearchTreeMap.Item(val)
        return BinarySearchTreeMap.Node(item)
    def restore_helper(prefix_stack, low, high):
        """
        low and high are the lower and upper bounds of the ranges
        Return the node of the next value is in range
        or None if stack is empty
        """
        #base case: if stack empty or out of range, return None
        if len(prefix_stack) == 0 or prefix_stack[-1] < low or prefix_stack[-1] > high:
            return None
        #recursive case: top element exists and is in range
        curr_val = prefix_stack.pop()
        node = make_node(curr_val)
        node.left = restore_helper(prefix_stack, low, curr_val)
        node.right = restore_helper(prefix_stack, curr_val, high)
        return node

    bst = BinarySearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    bst.root = restore_helper(prefix_lst[::-1], -float('inf'), float('inf'))
    bst.n = len(prefix_lst)
    return bst

# def main():
#     bst = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
#     for elem in bst:
#         print(elem, end=' ')# 1 3 5 7 9 11 13 15
#     print()
#
# main()
