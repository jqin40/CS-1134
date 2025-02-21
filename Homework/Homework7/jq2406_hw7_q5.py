from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    def create_expression_tree_helper(exp_lst, start_pos):
        '''Returns (root_node, size_of_subtree)'''
        #if operator
        if exp_lst[start_pos] in '+-*/':
            # bt = LinkedBinaryTree()
            # bt.root = exp_lst[start_pos]
            node = LinkedBinaryTree.Node(exp_lst[start_pos])
            Lnode, Lsize = create_expression_tree_helper(exp_lst, start_pos + 1)
            Rnode, Rsize = create_expression_tree_helper(exp_lst, start_pos + 1 + Lsize)
            node.left = Lnode
            node.right = Rnode
            return (node, 1+Lsize+Rsize)
        else: #integer
            node = LinkedBinaryTree.Node(int(exp_lst[start_pos]))
            return (node, 1)
    #edge case:
    if len(prefix_exp_str) == 0:
        return LinkedBinaryTree()

    exp_lst = prefix_exp_str.split()
    root, subtree_size = create_expression_tree_helper(exp_lst, 0)
    bt = LinkedBinaryTree(root)
    return bt

def prefix_to_postfix(prefix_exp_str):
    bt = create_expression_tree(prefix_exp_str)
    result = ''
    for node in bt.postorder():
        result += str(node.data) + ' '
    return result[:-1] #remove the last space

# def main():
#     #tests for 5a
#     bt = create_expression_tree('* 2 + - 15 6 4')
#     for node in bt:
#         print(node, end=' ') #breadth first should be: '* 2 + - 4 15 6'
#     print()
#
#     bt2 = create_expression_tree('')
#     for node in bt2:
#         print(node, end=' ') #nothing bc empty
#     print()
#
#     bt3 = create_expression_tree('+ 2 1')
#     for node in bt3:
#         print(node, end=' ') #+ 2 1
#     print()
#
#     #tests for 5b
#     print(prefix_to_postfix('* 2 + - 15 6 4')) #2 15 6 – 4 + *
#     print(prefix_to_postfix('+ 2 1')) #2 1 +
#     print(prefix_to_postfix('')) #empty
#
# main()