from collections import deque

class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (left is not None): #left has an element
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def count_nodes(self):
        def subtree_sum(root):
            if root is None:
                return 0
            else:
                left_count = subtree_sum(root.left)
                right_count = subtree_sum(root.right)
                return left_count + right_count + 1

        return subtree_sum(self.root)

    def height(self):
        def subtree_height(root):
            if (root.left is None and root.right is None):
                return 0 #no children
            elif root.right is None:
                left_height = subtree_height(root.left)
                return 1 + left_height
            elif root.left is None:
                right_height = subtree_height(root.right)
                return 1 + right_height
            else:
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if self.is_empty():
            raise Exception("Tree is empty")
        return subtree_height(self.root)

    def inorder(self):
        #LDR
        def subtree_inorder(root):
            if root is None:
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)
        yield from subtree_inorder(self.root)

def main():
    node1 = LinkedBinaryTree.Node(3)
    node2 = LinkedBinaryTree.Node(5)
    node3 = LinkedBinaryTree.Node(7)
    node4 = LinkedBinaryTree.Node(9)
    node5 = LinkedBinaryTree.Node(11)

    left_subtree = LinkedBinaryTree.Node(4, node1, node2)
    right_subtree = LinkedBinaryTree.Node(10, node3, node4)
    root = LinkedBinaryTree.Node(6, left_subtree, right_subtree)

    tree = LinkedBinaryTree(root)

    print("inorder traversal:")
    for node in tree.inorder():
        print(node.data, end =" , ")

main()
