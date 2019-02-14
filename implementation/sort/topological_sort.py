from queue import Queue


def sort(graph):
    queue = Queue()
    indegreeMap = {}
    sortedList = []

    for i in range(graph.numVertices):
        indegreeMap[i] = graph.get_indegree(i)

        # queue all node with no dependencies i.e no edge coming in
        if indegreeMap[i] == 0:
            queue.put(i)

    while not queue.empty():
        vertex = queue.get()
        sortedList.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegreeMap[v] = indegreeMap[v] - 1

            if indegreeMap[i] == 0:
                queue.put(i)

    if len(sortedList) != graph.numVertices:
        raise ValueError('This graph has a cycle')
