from LinkedBinaryTree import LinkedBinaryTree

def is_height_balanced(bin_tree):
    def subtree_is_hb(root):
        #Returns a tuple of (height, is_height_balanced)
        #base case: the None child has 0 height and is considered height-balanced
        if root is None:
            return (0, True)
        #recursive case:
        else:
            left = subtree_is_hb(root.left)
            right = subtree_is_hb(root.right)
            subheight = 1 + max(left[0], right[0])
            if (left[1] and right[1]): #if left and right children are balanced
                #balanced is the boolean whether left and right are at most 1 apart
                balanced = (-1 <= left[0]-right[0] <= 1)
            else: #at least one child is not height balanced
                balanced = False
            return (subheight, balanced)

    result = subtree_is_hb(bin_tree.root)
    return result[1]

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
#     print(is_height_balanced(bt)) #False, tree from Q1 is not height-balanced
#
#     bt2 = LinkedBinaryTree()
#     print(is_height_balanced(bt2)) #True, empty binary tree is height-balanced
#
#     bt3 = LinkedBinaryTree(node1)
#     print(is_height_balanced(bt3)) #True, binary tree with one node is height-balanced
#
#     node9 = LinkedBinaryTree.Node(9)
#     node10 = LinkedBinaryTree.Node(2, node9)
#     node11 = LinkedBinaryTree.Node(5)
#     node12 = LinkedBinaryTree.Node(1)
#     node13 = LinkedBinaryTree.Node(8, node11, node12)
#     node14 = LinkedBinaryTree.Node(4)
#     node15 = LinkedBinaryTree.Node(7, node13, node14)
#     node16 = LinkedBinaryTree.Node(3, node10, node15)
#     bt4 = LinkedBinaryTree(node16)
#     print(is_height_balanced(bt4)) #True
#
#     node17 = LinkedBinaryTree.Node(5)
#     node18 = LinkedBinaryTree.Node(1)
#     node19 = LinkedBinaryTree.Node(9, node17, node18)
#     node20 = LinkedBinaryTree.Node(2, node19)
#     node21 = LinkedBinaryTree.Node(8)
#     node22 = LinkedBinaryTree.Node(4)
#     node23 = LinkedBinaryTree.Node(7, node21, node22)
#     node24 = LinkedBinaryTree.Node(3, node20, node23)
#     bt5 = LinkedBinaryTree(node24)
#     print(is_height_balanced(bt5)) #False
#
# main()