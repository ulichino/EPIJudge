from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_symmetric_helper(node_a, node_b):
    if not node_a and not node_b: # both are None
        return True
    if not node_a or not node_b: # one is None and the other isn't
        return False
    return node_a.data == node_b.data and is_symmetric_helper(node_a.left, node_b.right) and is_symmetric_helper(node_a.right, node_b.left)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    return is_symmetric_helper(tree, tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
