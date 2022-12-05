from typing import List
import doctest
import networkx as nx
import matplotlib.pyplot as plt

m1 = [[1, 1, 0.1, 0],
      [0, 0, 0.9, 1]]

m2 = [[0, 0.2, 0, 1],
      [1, 0.8, 0.87, 0]]

m3 = [[1, 0.1, 0.07, 0],
      [0, 0.2, 0.93, 1]]

m4 = [[0.2, 1, 0, 1],
      [0.72, 0, 0.87, 0],
      [0.08, 0, 0.13, 0]]

m5 = [[0, 0.2, 0.13, 0.5, 0.1],
      [0.2, 0.8, 0.37, 0.5, 0.4],
      [0.8, 0, 0.5, 0, 0.4]]

m6 = [[1, 0, 0, 1],
      [0, 0, 1, 0],
      [1, 1, 0, 0],
      [0, 0, 0, 1]]

m7 = [[0, 0.2, 0.13, 0.5, 0.1],
      [0.2, 0.4, 0, 0.5, 0.4],
      [0.25, 0, 0.07, 0, 0.4],
      [0.25, 0.4, 0.3, 0, 0],
      [0.3, 0, 0.5, 0, 0.1]]


def find_cycle_in_consumption_graph(allocation: List[List[float]]):
    """
    >>> find_cycle_in_consumption_graph(m1)
    No circle found
    >>> find_cycle_in_consumption_graph(m2)
    No circle found
    >>> find_cycle_in_consumption_graph(m3)
    [(4, 1), (1, 5), (5, 2), (2, 4)]
    >>> find_cycle_in_consumption_graph(m4)
    [(0, 5), (5, 2), (2, 6), (6, 0)]
    >>> find_cycle_in_consumption_graph(m5)
    [(2, 6), (6, 0), (0, 7), (7, 2)]
    >>> find_cycle_in_consumption_graph(m6)
    No circle found
    >>> find_cycle_in_consumption_graph(m7)
    [(1, 5), (5, 2), (2, 7), (7, 0), (0, 6), (6, 1)]
    """
    p_len = len(allocation)  # Number of Players
    o_len = len(allocation[0])  # Number of Objects
    graph = nx.Graph()
    for i in range(p_len):  # Players
        for j in range(o_len):  # Objects
            if 0 < allocation[i][j] <= 1:
                graph.add_edge(j, i + o_len)
    # nx.draw(graph)
    # plt.show()
    try:
        print(nx.find_cycle(graph))
    except:
        print('No circle found')


if __name__ == "__main__":
    print(doctest.testmod())
