from BinarySearchTreeMap import *

#question 4
def find_min_abs_difference(bst):
    """
    Returns the minimum absolute difference
    between keys of any two nodes in bst
    """
    # def subtree_mad(cursor):
    #     """
    #     Returns (max of the left subtree, min of right subtree, minimum difference) so far
    #     """
    #     #base case
    #     if cursor.left is None and cursor.right is None:
    #         return (cursor.item.key, cursor.item.key, None) #None is overwritten later
    #     #recursive case
    #     else:
    #         if cursor.right is None:
    #             left = subtree_mad(cursor.left)
    #             max_left = max(left[0],left[1])
    #             min_diff_left = left[2]
    #             diff = cursor.item.key - max_left
    #             if min_diff_left is not None:
    #                 diff = min(min_diff_left, diff)
    #             #diff is now the minimum abs difference over the left subtree
    #             return (max_left, cursor.item.key, diff) #treat cursor as the min of right subtree
    #         elif cursor.left is None:
    #             right = subtree_mad(cursor.right)
    #             min_right = min(right[0],right[1])
    #             min_diff_right = right[2]
    #             diff = min_right - cursor.item.key
    #             if min_diff_right is not None:
    #                 diff = min(min_diff_right, diff)
    #             #diff is now the minimum abs difference over the right subtree
    #             return (cursor.item.key, min_right, diff) #treat cursor as the max of the left subtree
    #         else: #cursor.left and cursor.right are not None
    #             left = subtree_mad(cursor.left)
    #             max_left = max(left[0], left[1])
    #             min_diff_left = left[2]
    #             diffL = cursor.item.key - max_left
    #             if min_diff_left is not None:
    #                 diffL = min(min_diff_left, diffL)
    #                 #diffL is now the minimum abs difference over the left subtree
    #             right = subtree_mad(cursor.right)
    #             min_right = min(right[0], right[1])
    #             min_diff_right = right[2]
    #             diffR = min_right - cursor.item.key
    #             if min_diff_right is not None:
    #                 diffR = min(min_diff_right, diffR)
    #                 #diffR is now the minimum abs difference over the right subtree
    #             return (cursor.item.key, min_right, min(diffL, diffR)) #treat cursor as the max of the left subtree
    # #edge case
    # if bst.root is None:
    #     return None
    # return subtree_mad(bst.root)[2]
    if len(bst) == 0 or len(bst) == 1: return None
    in_order = [key for key in bst]
    minimum = in_order[1] - in_order[0]
    for i in range(1, len(in_order)-2):
        diff = in_order[i+1] - in_order[i]
        if diff < minimum:
            minimum = diff
    return minimum

# def main():
#     bst = BinarySearchTreeMap()
#     bst.insert(9, None)
#     bst.insert(7, None)
#     bst.insert(20, None)
#     bst.insert(4, None)
#     bst.insert(17, None)
#     bst.insert(25, None)
#     bst.insert(1, None)
#     bst.insert(6, None)
# #     for elem in bst:
# #         print(elem, end=' ')# 1 4 6 7 9 17 20 25
# #     print()
#     print(find_min_abs_difference(bst)) #1 because min difference between 6 and 7 is 1
#
# main()
