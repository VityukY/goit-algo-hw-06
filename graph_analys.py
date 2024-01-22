import networkx as nx
from metro_graph import metro_graph
from collections import deque
from BFS import bfs_recursive
from DFS import dfs_recursive

import matplotlib.pyplot as plt


stations = metro_graph.number_of_nodes()
connections = metro_graph.number_of_edges()

with open("readme.md", "w", encoding="utf-8") as fp:
    fp.write(f"Київське метро складається з {stations} станцій\n")
    fp.write(f"Київське метро має {connections} прокладених зєднань\n\n\n")

adjacency_list = nx.to_dict_of_lists(metro_graph)

dfs_result = dfs_recursive(metro_graph, "Akademmistechko")
station_str = "\n".join([station for station in dfs_result])
print(type(dfs_result))

bfs_result = bfs_recursive(adjacency_list, deque(["Akademmistechko"]))
station_str = "\n".join([station for station in dfs_result])
print(type(bfs_result))

with open("readme.md", "a", encoding="utf-8") as fp:
    fp.write(
        "Маршрути складені для аналізу методами BFS і DFS ідентичні до першої пересадки. Один з маршуртів продовжую шлях по гілці, другий пересаджується при першій же можливості\n"
    )
    fp.write(f"| {'dfs_result':<30} | {'bfs_result':<30} |\n")
    total_width = 30 * 2 + 3
    fp.write("-" * total_width + "\n")

    for item1, item2 in zip(dfs_result, bfs_result):
        fp.write(f"| {item1:<30} | {item2:<30} |\n")
    fp.writelines("\n\n")

# Застосування алгоритму Дейкстри

shortest_path_lengths = nx.single_source_dijkstra_path_length(
    metro_graph, source="Akademmistechko"
)


def print_line(width):
    print("-" * (width * 2 + 3))


with open("readme.md", "a", encoding="utf-8") as fp:
    fp.write(
        "Обравши місце відправлення ми можемо за допомогою метода Дейсктри отримати відомості, за який проміжок часу зможем добратись до будь-якої станції\n"
    )
    fp.write("-" * (25 * 2 + 3) + "\n")
    fp.write(f"| {'Station':<30} | {'Travel time (min)':<20} |\n")
    fp.write("-" * (25 * 2 + 3) + "\n")

    for station, travel_time in shortest_path_lengths.items():
        fp.write(f"| {station:<30} | {travel_time:<20} |\n")

    fp.write("-" * (25 * 2 + 3))


plt.show()
