from implementation.sort import *
from implementation.adjacency_matrix_graph import AdjacencyMatrixGraph

graph = AdjacencyMatrixGraph(9, directed=True)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 7)
graph.add_edge(2, 4)
graph.add_edge(2, 3)
graph.add_edge(1, 5)
graph.add_edge(5, 6)
graph.add_edge(3, 6)
graph.add_edge(3, 4)
graph.add_edge(6, 8)

sort(graph)
