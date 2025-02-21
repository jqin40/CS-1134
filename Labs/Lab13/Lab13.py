from BinarySearchTreeMap import *
#1.
def min_max_BST(bst):
    if bst.root is None: return (None, None)
    cursor = bst.root
    while cursor.left is not None:
        cursor = cursor.left
    min_key = cursor.item.key
    cursor = bst.root
    while cursor.right is not None:
        cursor = cursor.right
    max_key = cursor.item.key
    return (min_key, max_key)
#answer
# def min_max_BST(bst):
#     minimum = bst.root
#     maximum = bst.root
#     while minimum.left is not None:
#         minimum = minimum.left
#     while maximum.right is not None:
#         maximum = maximum.right
#     return (minimum.item.key, maximum.item.key)

# def main1():
#     bst = BinarySearchTreeMap()
#     bst[5] = None
#     bst[2] = None
#     bst[1] = None
#     bst[3] = None
#     bst[12] = None
#     bst[9] = None
#     bst[21] = None
#     bst[19] = None
#     bst[25] = None
#     print(min_max_BST(bst)) #(1, 25)
#
# main1()

#2.
def glt_n(bst, n):
    if bst.root is None: return -1
    cursor = bst.root
    parent = None
    while cursor is not None:
        if n == cursor.item.key: return n
        elif n > cursor.item.key:
            parent = cursor
            cursor = cursor.right
        else: #n < cursor.item.key
            if parent and n > parent.item.key:
                return parent.item.key
            else: #n < cursor and (parent is root or n < parent)
                parent = cursor
                if cursor.left: cursor = cursor.left
                else: return -1 #n is less than everything in the tree
    #cursor is reaches a None
    return parent.item.key

# def main2():
#     bst = BinarySearchTreeMap()
#     bst[5] = None
#     bst[2] = None
#     bst[1] = None
#     bst[3] = None
#     bst[12] = None
#     bst[9] = None
#     bst[21] = None
#     bst[19] = None
#     bst[25] = None
#     print(glt_n(bst, 21)) #21
#     print(glt_n(bst, 4)) #3
#     print(glt_n(bst, 26)) #25
#     print(glt_n(bst, 0)) #-1 because less than everything
#
# main2()

#3.
def compare_BST(bst1, bst2):
    '''
    Returns true if the two binary search trees contain the same set of elements and false if not
    '''
    if len(bst1) != len(bst2): return False
    key_lst1 = []
    for key in bst1:
        key_lst1.append(key)
    #alternative list comprehension syntax: key_lst1 = [key for key in bst]
    key_lst2 = []
    for key in bst2:
        key_lst2.append(key)
    #check if elements match
    for i in range(len(bst1)):
        if key_lst1[i] != key_lst2[i]:
            return False
    return True

# def main3():
#     bst1 = BinarySearchTreeMap()
#     bst1[15] = None
#     bst1[10] = None
#     bst1[20] = None
#     bst1[5] = None
#     bst1[12] = None
#     bst1[25] = None
#
#     bst2 = BinarySearchTreeMap()
#     bst2[15] = None
#     bst2[12] = None
#     bst2[20] = None
#     bst2[5] = None
#     bst2[25] = None
#     bst2[10] = None
#
#     print(compare_BST(bst1, bst2))
#
# main3()

#4.
def is_BST(root):
    return is_BST_helper(root)[2]

def is_BST_helper(root):
    '''Returns a tuple (min,max,bool)'''
    #edge case
    if root is None:
        return (None, None, True)

    val = root.item.key
    #base case
    if root.left is None and root.right is None:
        return (val, val, True)
    #recursive case
    elif root.left and root.right:
        Lmin, Lmax, Lbool = is_BST_helper(root.left)
        Rmin, Rmax, Rbool = is_BST_helper(root.right)
        are_subtrees_valid = Lmax < val < Rmin
        return (Lmin, Rmax, Lbool and Rbool and are_subtrees_valid)
    elif root.left:
        Lmin, Lmax, Lbool = is_BST_helper(root.left)
        is_subtree_valid = Lmax < val
        return (Lmin, val, Lbool and is_subtree_valid)
    else: #root.right exists
        Rmin, Rmax, Rbool = is_BST_helper(root.right)
        is_subtree_valid = val < Rmin
        return (val, Rmax, Rbool and is_subtree_valid)

# def main4():
#     bst = BinarySearchTreeMap()
#     bst[5] = None
#     bst[2] = None
#     bst[1] = None
#     bst[3] = None
#     bst[12] = None
#     bst[9] = None
#     bst[21] = None
#     bst[19] = None
#     bst[25] = None
#     print(is_BST(bst.root)) #True
#
# main4()

