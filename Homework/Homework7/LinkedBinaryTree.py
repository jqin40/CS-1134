from ArrayQueue import ArrayQueue

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return 1 + left_count + right_count

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return root.data + left_sum + right_sum

        return subtree_sum(self.root)


    def height(self):
        def subtree_height(root):
            if (root.left is None and root.right is None):
                return 0
            elif (root.left is None):
                return 1 + subtree_height(root.right)
            elif (root.right is None):
                return 1 + subtree_height(root.left)
            else:
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

    #Question 2
    def leaves_list(self):
        def leaf_generator(root):
            # base case: left and right are both None
            if root.left is None and root.right is None:
                yield root.data
            # recursive case: left not None, right not None
            else:
                if root.left is not None:
                    yield from leaf_generator(root.left)
                if root.right is not None:
                    yield from leaf_generator(root.right)
        #edge case:
        if self.is_empty(): return []

        return list(leaf_generator(self.root))

    #Question 4
    def iterative_inorder(self):
        '''No recursion, no helper methods, theta(1) memory, linear runtime'''
        cursor = self.root
        prev = None #None is the root's parent
        while cursor is not None:
            if prev == cursor.parent:
                if cursor.left is not None:
                    prev = cursor
                    cursor = cursor.left
                else:
                    yield cursor.data
                    if cursor.right is not None:
                        prev = cursor
                        cursor = cursor.right
                    else:
                        prev, cursor = cursor, prev
            elif prev == cursor.left:
                yield cursor.data
                if cursor.right is not None:
                    prev = cursor
                    cursor = cursor.right
                else:
                    prev = cursor
                    cursor = cursor.parent
            else: #prev == cursor.right
                prev = cursor
                cursor = cursor.parent

#tests for question 4
# def main4():
    # #tree from q1
    # node1 = LinkedBinaryTree.Node(5)
    # node2 = LinkedBinaryTree.Node(1)
    # node3 = LinkedBinaryTree.Node(9, node1, node2)
    # node4 = LinkedBinaryTree.Node(8)
    # node5 = LinkedBinaryTree.Node(4)
    # node6 = LinkedBinaryTree.Node(7, node4, node5)
    # node7 = LinkedBinaryTree.Node(2, node3)
    # node8 = LinkedBinaryTree.Node(3, node7, node6)
    # bt = LinkedBinaryTree(node8)
    # for item in bt.iterative_inorder():
    #     print(item, end=' ') #5 9 1 2 3 8 7 4
    # print()
    #
    # bt2 = LinkedBinaryTree()
    # for item in bt2.iterative_inorder():
    #     print(item, end=' ') #nothing
    # print()
    #
    # node9 = LinkedBinaryTree.Node(1)
    # bt3 = LinkedBinaryTree(node9)
    # for item in bt3.iterative_inorder():
    #     print(item, end=' ') #1
    # print()

    #tree I made with mostly right branches
    # node10 = LinkedBinaryTree.Node(5)
    # node11 = LinkedBinaryTree.Node(4, None, node10)
    # node12 = LinkedBinaryTree.Node(3, None, node11)
    # node13 = LinkedBinaryTree.Node(2, None, node12)
    # node14 = LinkedBinaryTree.Node(7)
    # node15 = LinkedBinaryTree.Node(6, None, node14)
    # node16 = LinkedBinaryTree.Node(1, node13, node15)
    # bt4 = LinkedBinaryTree(node16)
    # for item in bt4.iterative_inorder():
    #     print(item, end=' ') #2 3 4 5 1 6 7
    # print()

    #tree if root has no right
    # node17 = LinkedBinaryTree.Node(3)
    # node18 = LinkedBinaryTree.Node(2, None, node17)
    # node20 = LinkedBinaryTree.Node(20)
    # node19 = LinkedBinaryTree.Node(1, node18, node20)
    # bt5 = LinkedBinaryTree(node19)
    # for item in bt5.iterative_inorder():
    #     print(item, end=' ') #2 3 1 20
    # print()

# main4()

#tests for question 2
# def main2():
#     node1 = LinkedBinaryTree.Node(5)
#     node2 = LinkedBinaryTree.Node(1)
#     node3 = LinkedBinaryTree.Node(9, node1, node2)
#     node4 = LinkedBinaryTree.Node(8)
#     node5 = LinkedBinaryTree.Node(4)
#     node6 = LinkedBinaryTree.Node(7, node4, node5)
#     node7 = LinkedBinaryTree.Node(2, node3)
#     node8 = LinkedBinaryTree.Node(3, node7, node6)
#     bt = LinkedBinaryTree(node8)
#     print(bt.leaves_list()) #[5,1,8,4]
#
#     bt2 = LinkedBinaryTree()
#     print(bt2.leaves_list()) #[]
#
#     bt3 = LinkedBinaryTree(node1)
#     print(bt3.leaves_list()) #[5]
#
# if __name__ == '__main__':
#     main2()