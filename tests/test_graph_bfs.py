from ..Graph import Graph
from .. import graph_bfs
import unittest


def make_basic_graph():
    root = Graph(1)

    n_1 = Graph(2)
    n_2 = Graph(4)
    n_1.add_neighbor(n_2)

    root.add_neighbor(n_1)
    root.add_neighbor(Graph(3))
    root.add_neighbor(n_2)
    return root


class TestGraphBFS(unittest.TestCase):
    def test_graph_bfs_std(self):
        root = make_basic_graph()
        ret = graph_bfs.bfs(root)
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, ret)

    def test_graph_bfs_none(self):
        root = None
        ret = graph_bfs.bfs(root)
        expected = []
        self.assertEqual(expected, ret)