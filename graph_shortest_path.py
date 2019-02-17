from implementation.adjacency_set_graph import AdjacencySetGraph
from implementation.shortest_path import shortest_path, dikstras_shortest_path

graph = AdjacencySetGraph(8, directed=True)

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

graph_two = AdjacencySetGraph(8, directed=False)

graph_two.add_edge(0, 1, 1)
graph_two.add_edge(1, 2, 2)
graph_two.add_edge(1, 3, 6)
graph_two.add_edge(2, 3, 2)
graph_two.add_edge(1, 4, 3)
graph_two.add_edge(3, 5, 1)
graph_two.add_edge(5, 4, 5)
graph_two.add_edge(3, 6, 1)
graph_two.add_edge(6, 7, 1)
graph_two.add_edge(0, 7, 8)

dikstras_shortest_path(graph_two, 0, 6)
dikstras_shortest_path(graph_two, 4, 7)
dikstras_shortest_path(graph_two, 7, 0)
