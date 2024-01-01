from src.datastruct.graph import *
from src.datastruct import graphviz


if __name__ == '__main__':
    s = """7, 8
        0, 1
        0, 2
        1, 3
        1, 4
        2, 3
        2, 6
    """
    g = Graph.load(s)
    print(g)
    print(list(travel(g)))
    graphviz.adjlist_graph(g)