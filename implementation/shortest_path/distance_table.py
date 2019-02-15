from queue import Queue


def build_distance_table(graph, source):
    queue = Queue()

    # (distance form source, last vertex on path from source)
    distance_table = {}

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    distance_table[source] = (0, source)
    queue.put(source)

    while not queue.empty():
        current_vertex = queue.get()

        current_distance = distance_table[current_vertex][0]

        for neighbour in graph.get_adjacent_vertices(current_vertex):
            if distance_table[neighbour][0] is None:
                distance_table[neighbour] = (
                    1 + current_distance, current_vertex)

                if len(graph.get_adjacent_vertices(neighbour)) > 0:
                    queue.put(neighbour)

    return distance_table
