class Graph:
    def __init__(self, value=None):
        self.val = value
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=1):
        """
        Adds a neighbor to the neighbors dictionary
        :param neighbor: Instance of the graph class as a neighbor
        :param weight: Weight of the edge between neighbors
        :return:
        """
        self.neighbors[neighbor] = weight
