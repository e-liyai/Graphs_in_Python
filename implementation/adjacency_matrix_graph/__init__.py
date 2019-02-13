########################################################
#
# Representation of a Graph for adjacency metrix
#
########################################################
import numpy as np

from implementation.base_graph import Graph


class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError('Vertices %d and %d are out of bounds' % (v1, v2))

        if weight < 1:
            raise ValueError('An edge cannot have weight < 1')

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v1][v2] = weight

    def get_adjacent_vertices(self, v):
        self.check_valid_vartices(v)

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        self.check_valid_vartices(v)

        in_degree = 0
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                in_degree += 1

        return in_degree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, ' -----> ', v)

    def check_valid_vartices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError('Cannot access vertices %d' % v)
