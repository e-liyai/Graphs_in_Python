########################################################
#
# base class representation of a Graph with allt the
# interface methods
#
########################################################

import abc
import numpy as np


class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractMethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractMethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractMethod
    def get_indegree(self, v):
        pass

    @abc.abstractMethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractMethod
    def display(self):
        pass
