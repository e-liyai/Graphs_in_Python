from implementation.adjacency_set_graph import AdjacencySetGraph
from implementation.shortest_path import shortest_path

graph = AdjacencySetGraph(8)

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(1, 4)
graph.add_edge(3, 5)
graph.add_edge(5, 4)
graph.add_edge(3, 6)
graph.add_edge(6, 7)
graph.add_edge(0, 7)

shortest_path(graph, 0, 5)
shortest_path(graph, 0, 6)
shortest_path(graph, 7, 4)
