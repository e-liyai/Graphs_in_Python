from implementation.shortest_path.dikstras_priority_queue import priority_dict


def build_dikstras_distance_table(graph, source):

    distance_table = {}

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    distance_table[source] = (0, source)

    priority_queue = priority_dict()

    priority_queue[source] = 0

    while len(priority_queue.keys()) > 0:

        current_vertex = priority_queue.pop_smallest()
        current_distance = priority_queue[current_vertex][0]

        for neighbour in graph.get_adjacent_vertices(current_vertex):
            distance = current_distance + \
                graph.get_edga_weight(current_vertex, neighbour)

            neighbour_distance = distance_table[neighbour][0]

            if neighbour_distance is None or neighbour_distance > distance:
                distance_table[neighbour] = (distance, current_vertex)
                priority_queue[neighbour] = distance

    return distance_table
