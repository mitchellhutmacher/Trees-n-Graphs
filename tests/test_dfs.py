from ..Tree import Tree
from .. import dfs
import unittest


def make_basic_tree():
    """
    Makes a basic tree for testing.
    :return: Pointer to root node of the newly created tree
    """
    root = Tree(4)
    root.left = Tree(2)
    root.left.left = Tree(1)
    root.left.right = Tree(3)
    root.right = Tree(6)
    root.right.left = Tree(5)
    root.right.right = Tree(7)
    return root


class TestDfs(unittest.TestCase):
    def test_pre_order_std(self):
        root = make_basic_tree()
        dfs_arr = dfs.pre_order(root, [])
        expected = [4, 2, 1, 3, 6, 5, 7]
        self.assertEqual(dfs_arr, expected)

    def test_pre_order_none(self):
        root = None
        dfs_arr = dfs.pre_order(root)
        expected = []
        self.assertEqual(dfs_arr, expected)

    def test_in_order_std(self):
        root = make_basic_tree()
        dfs_arr = dfs.in_order(root, [])
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(dfs_arr, expected)

    def test_in_order_none(self):
        root = None
        dfs_arr = dfs.in_order(root, [])
        expected = []
        self.assertEqual(dfs_arr, expected)


if __name__ == "__main__":
    unittest.main()
