from LinkedBinaryTree import LinkedBinaryTree
#1 in LBT
#2.
def is_perfect(root):
    '''Returns True if the Binary Tree is perfect and false if not
    Using recursion'''
    #base
    if root is None:
        return (True,0) #whether perfect, max_depth
    #rec case
    is_left_perfect, left_depth = is_perfect(root.left)
    is_right_perfect, right_depth = is_perfect(root.right)

    is_root_perfect = (is_left_perfect and is_right_perfect and left_depth == right_depth)
    return (is_root_perfect, max(left_depth, right_depth) + 1)

def main():
    node1 = LinkedBinaryTree.Node(14)
    node2 = LinkedBinaryTree.Node(5)
    node3 = LinkedBinaryTree.Node(13, node1, node2)
    node4 = LinkedBinaryTree.Node(12)
    # node5 = LinkedBinaryTree.Node(7)
    node6 = LinkedBinaryTree.Node(9, node4,)
    node7 = LinkedBinaryTree.Node(8)
    node8 = LinkedBinaryTree.Node(15)
    node9 = LinkedBinaryTree.Node(3, node7, node8)
    node10 = LinkedBinaryTree.Node(1)
    node11 = LinkedBinaryTree.Node(4)
    node12 = LinkedBinaryTree.Node(6, node10, node11)
    node13 = LinkedBinaryTree.Node(2, node3, node6)
    node14 = LinkedBinaryTree.Node(11, node9, node12)
    node15 = LinkedBinaryTree.Node(10, node13, node14)
    # bt = LinkedBinaryTree(node15)

    print(is_perfect(node15))

main()