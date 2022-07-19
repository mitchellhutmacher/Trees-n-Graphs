from .Tree import Tree


def pre_order(root: Tree, order=[]):
    """
    Searches through the tree and returns the pre-order
    :param order: The pre-order of the tree
    :param root: Tree to be searched
    :return: Pre-order of the tree
    """
    if root is None:
        return order

    order.append(root.val)
    if root.left is None and root.right is None:
        return order
    else:
        if root.left is not None:
            order = pre_order(root.left, order)
        if root.right is not None:
            order = pre_order(root.right, order)
    return order


def in_order(root: Tree):
    """
    Searches through the tree and returns the in-order
    :param root: Tree to be searched
    :return: In-order of the tree
    """
    return None


def post_order(root: Tree):
    """
    Searches through the tree and returns the post-order
    :param root: Tree to be searched
    :return: Post-order of the tree
    """
    return None
