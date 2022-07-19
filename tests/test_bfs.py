from ..Tree import Tree
from .. import bfs
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


class TestBfs(unittest.TestCase):
    def test_bfs_queue_std(self):
        root = make_basic_tree()
        bfs_arr = bfs.bfs_queue(root)
        expected = [4, 2, 6, 1, 3, 5, 7]
        self.assertEqual(bfs_arr, expected)

    def test_bfs_queue_none(self):
        root = None
        bfs_arr = bfs.bfs_queue(root)
        expected = []
        self.assertEqual(bfs_arr, expected)


if __name__ == "__main__":
    unittest.main()
