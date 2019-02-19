from implementation.spanning_tree import *
from implementation.adjacency_matrix_graph import AdjacencyMatrixGraph

graph = AdjacencyMatrixGraph(8, directed=False)
graph.add_edge(0, 1, 1)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 3, 2)
graph.add_edge(2, 3, 2)
graph.add_edge(1, 4, 3)
graph.add_edge(3, 5, 1)
graph.add_edge(5, 4, 2)
graph.add_edge(3, 6, 1)
graph.add_edge(6, 7, 1)
graph.add_edge(7, 0, 1)

# prim_spanning_tree(graph, 1)
kruskal_spanning_tree(graph)
