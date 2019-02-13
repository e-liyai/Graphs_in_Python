import numpy as np

from implementation.base_graph import Graph
from implementation.node import Node


class AdjacencySetGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencySetGraph, self).__init__(numVertices, directed)

        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))

        def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError('Vertices %d and %d are out of bounds' % (v1, v2))

        if weight != 1:
            raise ValueError('An adjacency set cannot rep edge weight != 1')
