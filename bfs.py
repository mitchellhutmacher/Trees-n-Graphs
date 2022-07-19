from collections import deque
from .Tree import Tree


def bfs_queue(root: Tree):
    """

    :param root: Root node of the tree
    :return: Array of level order traversal of the tree
    """
    if root is None:
        return []
    q = deque()
    q.appendleft(root)
    ret = []
    while len(q) > 0:
        temp = q.popleft()
        ret.append(temp.val)
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)
    return ret
