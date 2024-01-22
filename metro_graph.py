import networkx as nx
import matplotlib.pyplot as plt


# Створення графу
metro_graph = nx.Graph()

# Додавання станцій та їх з'єднань для червоної лінії (М1)
red_line = [
    "Akademmistechko",
    "Zhytomyrska",
    "Sviatoshyn",
    "Nyvky",
    "Beresteiska",
    "Shuliavska",
    "Politekhnichnyi Instytut",
    "Vokzalna",
    "Universytet",
    "Teatralna",
    "Khreshchatyk",
    "Arsenalna",
    "Zviretska",
    "Hydropark",
    "Livoberezhna",
    "Darnytsia",
    "Chernihivska",
    "Lisova",
]
connections_red = [
    (red_line[i], red_line[i + 1], {"weight": 3}) for i in range(len(red_line) - 1)
]  # Приклад значень ваги
metro_graph.add_nodes_from(red_line)
metro_graph.add_edges_from(connections_red)

# Додавання станцій та їх з'єднань для синьої лінії (М2)
blue_line = [
    "Heroiv Dnipra",
    "Warshavska",
    "Obolon",
    "Petrovka",
    "Pochaina",
    "Tarasa Shevchenka",
    "Kontraktova Ploshcha",
    "Poshtova Ploshcha",
    "Maidan Nezalezhnosti",
    "Ploshcha UA Hero",
    "Olimpiiska",
    "Palats Ukraina",
    "Lubitska",
    "Demiivska",
    "holosiivska",
    "Vasilkivska",
    "Vistavkoviu Center",
    "Ipodrom",
    "Teremky",
]
connections_blue = [
    (blue_line[i], blue_line[i + 1], {"weight": 3}) for i in range(len(blue_line) - 1)
]  # Приклад значень ваги
metro_graph.add_nodes_from(blue_line)
metro_graph.add_edges_from(connections_blue)

# Додавання станцій та їх з'єднань для зеленої лінії (М3)
green_line = [
    "Syrets",
    "Dorohozhychi",
    "Lukianivska",
    "Lvivska Brama",
    "Vokzalna",
    "Zoloti Vorota",
    "Palac Sportu",
    "Klovska",
    "Pecherska",
    "Ploshcha UA Hero",
    "Vidubichi",
    "Teluchka",
    "Slavytuck",
    "Osokorky",
    "Pozniyaki",
    "Kharkivska",
    "Vurlucia",
    "Borispilska",
    "Chervonuy hutir",
]
connections_green = [
    (green_line[i], green_line[i + 1], {"weight": 3})
    for i in range(len(green_line) - 1)
]  # Приклад значень ваги
metro_graph.add_nodes_from(green_line)
metro_graph.add_edges_from(connections_green)

# Зв'язки для пересадок між лініями
ground_connections = [
    (
        "Zoloti Vorota",
        "Teatralna",
        {"weight": 5, "color": "yellow", "width": 2},
    ),  # Приклад значення ваги
    (
        "Khreshchatyk",
        "Maidan Nezalezhnosti",
        {"weight": 5, "color": "yellow", "width": 2},
    ),  # Приклад значення ваги
    (
        "Palac Sportu",
        "Ploshcha UA Hero",
        {"weight": 5, "color": "yellow", "width": 2},
    ),  # Приклад значення ваги
]


metro_graph.add_edges_from(ground_connections)

# Відображення графу
pos = nx.spring_layout(metro_graph, seed=22)  # Додаємо seed для фіксації позицій вузлів
edge_colors = [
    metro_graph[u][v]["color"] if "color" in metro_graph[u][v] else "gray"
    for u, v in metro_graph.edges()
]
edge_widths = [
    metro_graph[u][v]["width"] if "width" in metro_graph[u][v] else 1
    for u, v in metro_graph.edges()
]

nx.draw(
    metro_graph,
    pos,
    with_labels=True,
    font_size=8,
    node_size=500,
    node_color="skyblue",
    font_color="black",
    font_weight="bold",
    edge_color=edge_colors,
    width=edge_widths,
)

# Виведення ваги на з'єднаннях
edge_labels = nx.get_edge_attributes(metro_graph, "weight")
nx.draw_networkx_edge_labels(
    metro_graph,
    pos,
    edge_labels=edge_labels,
    font_color="red",
)

if __name__ == "__main__":
    plt.title(
        "Kyiv Metro Graph with Interchanges, Ground Connections, and Travel Time (in minutes)"
    )
    plt.show()

    stations = metro_graph.number_of_nodes()
    connections = metro_graph.number_of_edges()

    with open("kiyv_metro.md", "r+", encoding="utf-8") as fp:
        fp.writelines(f"Київське метро складається з {stations} станцій\n")
        fp.writelines(f"Київське метро має {connections} прокладених зєднань\n")
