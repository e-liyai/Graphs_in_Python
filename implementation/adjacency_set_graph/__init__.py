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

        self.vertex_list[v1].add_edge(v2)

        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):

        self.check_valid_vertex(v)

        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        self.check_valid_vertex(v)

        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1

        return indegree

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, ' -----> ', v)

    def get_edge_weight(self, v1, v2):
        return 1

    def check_valid_vertex(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError('Cannot access vertex %d' % v)
