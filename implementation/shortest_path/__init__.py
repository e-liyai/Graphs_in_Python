from queue import queue


def build_distance_table(graph, source):
	queue = queue()

    # (distance form source, last vertex on path from source)
    distance_table = {}

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    # distance to source from itself is 0
    distance_table[source] = (0, source)
    queue.put(source)

    while not queue.empty():
    	current_vertex = queue.get()

    	current_distance = distance_table[current_vertex][0]

