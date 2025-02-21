"""
Helper functions to create and display linked binary trees
"""

from LinkedBinaryTree import LinkedBinaryTree

# Taken from https://leetcode.com/discuss/interview-question/1954462/pretty-printing-binary-trees-in-python-for-debugging
def display_tree(root):
    """Display the tree in a human readable format."""
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)

def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
        line = '%s' % self.data
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if self.right is None:
        lines, n, p, x = _display_aux(self.left)
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if self.left is None:
        lines, n, p, x = _display_aux(self.right)
        s = '%s' % self.data
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(self.left)
    right, m, q, y = _display_aux(self.right)
    s = '%s' % self.data
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def create_lbt_from_list(lst):
    """Given a list, construct a linked binary tree.
    
    list is level order traversal of the tree with mandatory None values
    for empty nodes.

    Example:
        [4, None, 3, None, None, 1, 2] ->
            4_  
              \ 
              3 
             / \
             1 2
        [0, 1, 2, 3, 4, 5, 6] ->
             _0_
            /   \
            1   2
           / \ / \
           3 4 5 6
    """
    def create_nodes(lst, lst_index):
        """Recursively create nodes from end of list."""
        if len(lst) <= lst_index or lst[lst_index] is None:  # index out of bounds
            return None

        left_child_index  = 2 * lst_index + 1
        right_child_index = 2 * lst_index + 2

        left  = create_nodes(lst, left_child_index)
        right = create_nodes(lst, right_child_index)
        parent_node = LinkedBinaryTree.Node(lst[lst_index], left, right)

        return parent_node

    root_node = create_nodes(lst, 0)
    return LinkedBinaryTree(root_node)

if __name__ == "__main__":
    lbt = create_lbt_from_list([4, None, 3, None, None, 1, 2])
    """
    lbt =
        4
         \
          3
         / \
        1   2
    """
    display_tree(lbt.root)

    """
    Construct leaf nodes first and build up tree. Avoids having to
    explicitly set parent node pointers and left/right node pointers.
    """

    a = LinkedBinaryTree.Node(1)
    b = LinkedBinaryTree.Node(2)
    c = LinkedBinaryTree.Node(3, a, b)
    d = LinkedBinaryTree.Node(4, None, c)

    linked_tree = LinkedBinaryTree(d)

    """
    linked_tree =
        4 (root, d)
         \
          3 (c)
         / \
    (a) 1   2 (b)
    """
    display_tree(linked_tree.root)
