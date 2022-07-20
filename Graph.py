class Graph:
    def __init__(self, value=None, dir=False):
        self.val = value
        self.directed = dir
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight_to=1, weight_from=0):
        """
        Adds a neighbor to the neighbors dictionary
        :param weight_from: Weight of the edge from neighbor to self
        :param weight_to: Weight of the edge from self to neighbor, ignored if
                          this is not a directed graph
        :param neighbor: Instance of the graph class as a neighbor
        :return:
        """
        self.neighbors[neighbor] = weight_to

        # Handle directed
        if self.directed:
            # If the weight_from is 0, there is no backwards pointer
            if weight_from != 0:
                neighbor.neighbors[self] = weight_from
        else:
            neighbor.neighbors[self] = weight_to
