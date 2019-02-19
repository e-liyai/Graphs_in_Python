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

        if v1 in spanning_tree[v2]:
            continue

        vertex_pair = sorted([v1, v2])
        spanning_tree[vertex_pair[0]].add(vertex_pair[1])

        if has_cycle(spanning_tree):
            spanning_tree[vertex_pair[0]].remove(vertex_pair[1])
            continue

        num_edges += 1

        visited.add(v1)
        visited.add(v2)

    print('Visited vertices: ', visited)

    if len(visited) != graph.numVertices:
        print('minimum spanning tree not found')
    else:
        print('minimum spanning tree: ')
        for key, value in spanning_tree.items():
            print(key, ' ---> ', value)


def has_cycle(spanning_tree):

    for source in spanning_tree:
        q = []
        visited_vertices = set()

        q.append(source)
        while len(q) > 0:
            vertex = q.pop(0)

            if vertex in visited_vertices:
                return True
            visited_vertices.add(vertex)
            q.extend(spanning_tree[vertex])

    return False
