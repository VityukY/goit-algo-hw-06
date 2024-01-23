def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        global visited_list
        visited_list = []
        visited = set()
    visited.add(vertex)
    visited_list.append(vertex)
    # print(vertex, end=" ")  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited_list
