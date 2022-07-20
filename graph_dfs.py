from .Graph import Graph


def dfs(root: Graph, visited, ret):
    """
    Recursive DFS algorithm
    :param root: Graph node from which to search
    :param visited: Set of nodes already seen
    :param ret: Return array - just the DFS order of elements
    :return: The order of visited elements
    """
    if root is not None:
        visited.add(root)
        ret.append(root.val)
        for neighbor in root.neighbors:
            if neighbor not in visited:
                ret = dfs(neighbor, visited, ret)
    return ret
