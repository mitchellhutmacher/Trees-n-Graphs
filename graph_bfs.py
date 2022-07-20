from .Graph import Graph
from collections import deque


def bfs(root: Graph):
    """
    Basic BFS on an undirected, unweighted graph
    :param root: Node of the graph from which to start
    :return: Values of the graph in BFS order
    """
    if root is None:
        return []
    q = deque()
    q.append(root)

    visited = set()
    visited.add(root)

    ret = []

    while len(q) > 0:
        temp = q.popleft()
        ret.append(temp.val)
        for neighbor in temp.neighbors:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

    return ret
