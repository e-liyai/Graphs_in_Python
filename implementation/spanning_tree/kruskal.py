from implementation.shortest_path import priority_dict


def kruskal_spanning_tree(graph):

    priority_queue = priority_dict()
    visited = set()
    spanning_tree = {}

    for v in range(graph.numVertices):
        for neighbour in graph.get_adjacent_vertices(v):
            priority_queue[(v, neighbour)] = graph.get_edge_weight(
                v, neighbour)

    for v in range(graph.numVertices):
        spanning_tree[v] = set()

    num_edges = 0

    while len(priority_queue.keys()) > 0 and num_edges < graph.numVertices - 1:

        v1, v2 = priority_queue.pop_smallest()
