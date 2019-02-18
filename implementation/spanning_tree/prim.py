from implementation.shortest_path import priority_dict


def prim_spanning_tree(graph, source):

    distance_table = {}
    priority_queue = priority_dict()

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    distance_table[source] = (0, source)
    priority_queue[source] = 0

    visited_vertices = set()

    # '1->2' representation of edges connecting two vertices 1 and 2
    spanning_tree = set()

    while len(priority_queue.keys()) > 0:
        current_vertex = priority_queue.pop_smallest()

        if current_vertex in visited_vertices
