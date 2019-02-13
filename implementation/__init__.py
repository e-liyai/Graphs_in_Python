########################################################
#
# A single node in a graph
#
########################################################


class Node:

    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError('Vertex %d cannot be adjacent to itself' % v)

        self.adjacency_set.add(v)

    def get_adjacent_verties(self):
        return sorted(self.adjacency_set)
