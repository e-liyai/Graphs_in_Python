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

        if current_vertex in visited_vertices:
            continue

        visited_vertices.add(current_vertex)

        if current_vertex != source:
            last_vertex = distance_table[current_vertex][1]
            edge = str(last_vertex) + '-->' + str(current_vertex)

            if edge not in spanning_tree:
                spanning_tree.add(edge)

        for neighbour in graph.get_adjacent_vertices(current_vertex):

            distance = graph.get_edge_weight(current_vertex, neighbour)
            neighbour_distance = distance_table[neighbour][0]

            if neighbour_distance is None or neighbour_distance > distance:
                distance_table[neighbour] = (distance, current_vertex)
                priority_queue[neighbour] = distance

    for edge in spanning_tree:
        print(edge)
