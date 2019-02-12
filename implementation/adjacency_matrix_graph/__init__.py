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
