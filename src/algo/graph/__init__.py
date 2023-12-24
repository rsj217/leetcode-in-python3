from src.datastruct.adj_list_graph import AdjListGraph
from src.datastruct import graphviz


def _build_disconnect_graph() -> AdjListGraph:
    """
    0 ----- 1
    |      / \
    |     /   \
    2 -- 3     4
     \
      6      5
    """
    s = """7, 6
        0, 1
        0, 2
        1, 3
        1, 4
        2, 3
        2, 6
    """
    
    return AdjListGraph.load(s)


def _build_connect_graph() -> AdjListGraph:
    """
    0 ----- 1
    |      / \
    |     /   \
    2 -- 3     4
     \    \
      6 -- 5
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
    return AdjListGraph.load(s)


def _build_without_circle_graph() -> AdjListGraph:
    """
    0 ----- 1
    |      / \
    |     /   \
    2    3     4
     \
      6     5
    """
    s = """7, 6
        0, 1
        0, 2
        1, 3
        1, 4
        2, 6
    """
    return AdjListGraph.load(s)


def _build_bipartite_graph() -> AdjListGraph:
    s = """7,7
    0, 1
    0, 2
    1, 3
    1, 4
    2, 3
    2, 6
    5, 6
    """
    return AdjListGraph.load(s)


def _build_unbipartite_graph() -> AdjListGraph:
    s = """4, 6
    0, 1
    0, 2
    0, 3
    1, 2
    1, 3
    2, 3
    """
    return AdjListGraph.load(s)


def show_disconnect_graph(g: AdjListGraph):
    print(g)
    graphviz.adjlist_graph(g)
