import unittest
from ..Graph import Graph
from .. import graph_dfs
from .test_graph_bfs import make_basic_graph


class TestDFS(unittest.TestCase):
    def test_dfs_std(self):
        root = make_basic_graph()
        expected = [1, 2, 4, 3]
        ret = graph_dfs.dfs(root, set(), [])
        self.assertEqual(expected, ret)

    def test_dfs_none(self):
        root = None
        expected = []
        ret = graph_dfs.dfs(root, set(), [])
        self.assertEqual(expected, ret)
