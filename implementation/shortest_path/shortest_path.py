from implementation.shortest_path.distance_table import build_distance_table


def shortest_path(graph, source, destination):

    distance_table = build_distance_table(graph, source)

    path = [destination]
    previous_vertex = distance_table[destination][1]

    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]

    if previous_vertex is None:
        print('There is no path from %d to %d' % (source, destination))
    else:
        path = [source] + path
        print('Shortest path is: ', path)
