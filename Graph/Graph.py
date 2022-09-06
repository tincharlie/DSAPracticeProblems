def BFS(graph, source):
    visited = [False] *  len(graph.data)
    queue = []

    visited[source] = True
    queue.append(source)

    i = 0
    while i < len(queue):
        for v in graph.data[queue[i]]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
        i += 1

    return queue

