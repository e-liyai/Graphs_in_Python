from queue import Queue
import numpy as np


def depth_first_search(graph, visited, current=0):

    if visited[current] == 1:
        return

    visited[current] = 1
    print('Visited: ', current)

    for vertex in graph.get_adjacent_vertices(current):
        depth_first_search(graph, visited, vertex)
