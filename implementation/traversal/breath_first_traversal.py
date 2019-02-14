from queue import Queue

from implementation.adjacency_set_graph import AdjacencySetGraph
from implementation.adjacency_matrix_graph import AdjacencyMatrixGraph


def breath_firsr_search(graph, start=0):

    queue = Queue()
    queue.start(start)
