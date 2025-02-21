from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        #base case: left and right are both None
        if root.left is None and root.right is None:
            return (root.data, root.data)
        #recursive case: left is None, right is None, or neither
        else:
            if root.left is None:
                right = subtree_min_and_max(root.right)
                minimum = min(right[0], root.data)
                maximum = max(right[1], root.data)
                return (minimum, maximum)
            elif root.right is None:
                left = subtree_min_and_max(root.left)
                minimum = min(left[0], root.data)
                maximum = max(left[1], root.data)
                return (minimum, maximum)
            else: #neither left or right is None
                left = subtree_min_and_max(root.left)
                right = subtree_min_and_max(root.right)
                minimum = min(left[0], right[0], root.data)
                maximum = max(left[1], right[1], root.data)
                return (minimum, maximum)

    if bin_tree.is_empty():
        raise Exception("Empty Tree")
    return subtree_min_and_max(bin_tree.root)


# def main():
#     node1 = LinkedBinaryTree.Node(5)
#     node2 = LinkedBinaryTree.Node(1)
#     node3 = LinkedBinaryTree.Node(9, node1, node2)
#     node4 = LinkedBinaryTree.Node(8)
#     node5 = LinkedBinaryTree.Node(4)
#     node6 = LinkedBinaryTree.Node(7, node4, node5)
#     node7 = LinkedBinaryTree.Node(2, node3)
#     node8 = LinkedBinaryTree.Node(3, node7, node6)
#     bt = LinkedBinaryTree(node8)
#     print(min_and_max(bt)) #(1,9)
#
#     # bt2 = LinkedBinaryTree()
#     # print(min_and_max(bt2)) #Exception
#
#     bt3 = LinkedBinaryTree(node1)
#     print(min_and_max(bt3))
#
# main()