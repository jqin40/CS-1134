#TODO: Question 4 of midterm prac
from LinkedBinaryTree import LinkedBinaryTree

#1.
def bt_even_sum(root):
    #base
    if root is None: return 0
    #recursive
    else:
        sum = 0
        if root.data % 2 == 0:
            sum += root.data
        sum += bt_even_sum(root.left) + bt_even_sum(root.right)
        return sum

# def main1():
#     node1 = LinkedBinaryTree.Node(7)
#     node2 = LinkedBinaryTree.Node(9)
#     node3 = LinkedBinaryTree.Node(2, node1, node2)
#     node4 = LinkedBinaryTree.Node(0)
#     root = LinkedBinaryTree.Node(4, node3, node4)
#     bt = LinkedBinaryTree(root)
#     print(bt_even_sum(root)) #6
#
# main1()

#2. in LinkedBinaryTree
# def main2():
#     node1 = LinkedBinaryTree.Node(7)
#     node2 = LinkedBinaryTree.Node(9)
#     node3 = LinkedBinaryTree.Node(2, node1, node2)
#     node4 = LinkedBinaryTree.Node(0)
#     root = LinkedBinaryTree.Node(4, node3, node4)
#     bt = LinkedBinaryTree(root)
#     print(0 in bt) #True
#     print(99 in bt) #False
#
# main2()

#3.
def is_full(root):
    '''Returns True if the Binary Tree is full
    and False if not'''
    def subtree_is_full(root):
        #edge case
        if root is None: return True #an empty tree is considered full because 0 children.

        #base case: 1 Node
        #True if no left and no right
        elif root.left is None and root.right is None: return True
        #False if only 1 between left and right doesnt exist
        elif root.left is None or root.right is None: return False
        #Both nodes nonempty
        else:
            return subtree_is_full(root.left) and subtree_is_full(root.right)
    return subtree_is_full(root)

# def main3():
#     node1 = LinkedBinaryTree.Node(7)
#     node2 = LinkedBinaryTree.Node(9)
#     node3 = LinkedBinaryTree.Node(2, node1, node2)
#     node4 = LinkedBinaryTree.Node(0)
#     root = LinkedBinaryTree.Node(4, node3, node4)
#     bt = LinkedBinaryTree(root)
#     print(is_full(bt.root)) #True
#
#     node5 = LinkedBinaryTree.Node(9)
#     node6 = LinkedBinaryTree.Node(11)
#     node7 = LinkedBinaryTree.Node(1, node5, node6)
#     node8 = LinkedBinaryTree.Node(4)
#     node9 = LinkedBinaryTree.Node(6, node7, node8)
#     node10 = LinkedBinaryTree.Node(3)
#     node11 = LinkedBinaryTree.Node(7, node10, node9)
#     bt2 = LinkedBinaryTree(node11)
#     print(is_full(bt2.root)) #True
#
# main3()