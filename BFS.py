from collections import deque


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        global visited_list
        visited_list = []
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return visited_list
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        visited_list.append(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    return bfs_recursive(graph, queue, visited)
