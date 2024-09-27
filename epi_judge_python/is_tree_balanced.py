from collections import namedtuple
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

BalancedAndHeight = namedtuple('BalancedAndHeight', 'balanced,height')

def is_balanced_helper(tree: BinaryTreeNode):
    if not tree:
        return BalancedAndHeight(True, 0)
    left = is_balanced_helper(tree.left)
    right = is_balanced_helper(tree.right)
    height = max(right.height, left.height)
    balanced = right.balanced and left.balanced and abs(right.height - left.height) <= 1
    return BalancedAndHeight(balanced, height + 1)


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return is_balanced_helper(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
