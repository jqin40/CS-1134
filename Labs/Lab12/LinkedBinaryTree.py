from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = None


    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)


    def count_nodes(self):
        def subtree_count(root):
            if(root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return left_count + right_count + 1

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if(root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return left_sum + right_sum + root.data

        return subtree_sum(self.root)


    def height(self):
        def subtree_height(root):
            if((root.left is None) and (root.right is None)):
                return 0
            elif(root.right is None): #left is not None
                left_height = subtree_height(root.left)
                return 1 + left_height
            elif(root.left is None): #right is not None
                right_height = subtree_height(root.right)
                return 1 + right_height
            else: #both subtrees are not None
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


    def preorder(self):
        def subtree_preorder(root):
            if(root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if(root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def breadth_first(self):
        if(self.is_empty()):
            return
        bfs_queue = ArrayQueue()
        bfs_queue.enqueue(self.root)
        while(bfs_queue.is_empty() == False):
            curr_node = bfs_queue.dequeue()
            yield curr_node
            if(curr_node.left is not None):
                bfs_queue.enqueue(curr_node.left)
            if(curr_node.right is not None):
                bfs_queue.enqueue(curr_node.right)


    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

    # 1 from Lab 12
    def preorder_with_stack(self):
        '''Returns a generator function that iterates through the tree
        using preorder traversal'''
        s = ArrayStack()
        #like base case
        s.push(self.root)
        while not s.is_empty():
            yield s.top().data
            temp = s.pop()
            #like recursive case
            if temp.right is not None:
                s.push(temp.right)
            if temp.left is not None:
                s.push(temp.left)


    #alt
    # node = s.pop()
    # yield node.data
    # if node.right is not None:
    #     s.push(node.right):
    # if node.left is not None:
    #     s.push(node.left)

def eval_exp_tree(exp_t):
    def subtree_eval_exp(root):
        if((root.left is None) and (root.right is None)):
            return root.data
        else:
            left_arg = subtree_eval_exp(root.left)
            right_arg = subtree_eval_exp(root.right)
            if (root.data == "+"):
                return left_arg + right_arg
            elif (root.data == "-"):
                return left_arg - right_arg
            if (root.data == "*"):
                return left_arg * right_arg
            if (root.data == "/"):
                return left_arg / right_arg

    return subtree_eval_exp(exp_t.root)

if __name__ == '__main__':
    node1 = LinkedBinaryTree.Node(5)
    node2 = LinkedBinaryTree.Node(11)
    node3 = LinkedBinaryTree.Node(6, node1, node2)
    node4 = LinkedBinaryTree.Node(2)
    node5 = LinkedBinaryTree.Node(7, node4, node3)
    node6 = LinkedBinaryTree.Node(4)
    node7 = LinkedBinaryTree.Node(9, node6)
    node8 = LinkedBinaryTree.Node(5, None, node7)
    node9 = LinkedBinaryTree.Node(2, node5, node8)
    t = LinkedBinaryTree(node9)

    for item in t.preorder_with_stack():
        print(item, end=' ')
    print()