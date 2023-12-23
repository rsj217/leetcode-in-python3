from src.datastruct.adj_list_graph import *
from src.datastruct import graphviz


if __name__ == '__main__':
    s = """7, 9
        0, 1
        0, 3
        1, 2
        1, 6
        2, 3
        2, 5
        3, 4
        4, 5
        5, 6
    """
    s = """7, 8
        0, 1
        0, 2
        1, 3
        1, 4
        2, 3
        2, 6
        3, 5
        5, 6
    """
    g = AdjListGraph.load(s)
    print(g)
    print(list(travel(g)))