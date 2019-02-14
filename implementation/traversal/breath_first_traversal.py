from queue import Queue
import numpy as np

from implementation.adjacency_set_graph import AdjacencySetGraph
from implementation.adjacency_matrix_graph import AdjacencyMatrixGraph


def breath_first_search(graph, start=0):

    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue

        print('Visit: ', vertex)
        visited[vertex] = 1

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)
