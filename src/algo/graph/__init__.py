from typing import Dict, Generator
from collections import deque
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


def dfs(g: AdjListGraph) -> Generator:
    def _dfs(v: int, visited: Dict[int, bool]) -> Generator:
        stack = [v]
        visited[v] = True
        while 0 < len(stack):
            v = stack.pop()
            yield v
            for w in g.adjs(v):
                if not visited[w]:
                    stack.append(w)
                    visited[w] = True
    
    visit = {k: False for k in g.adj}
    for k in g.adj:
        if not visit[k]:
            yield from _dfs(k, visit)


def bfs(g: AdjListGraph) -> Generator:
    def _bfs(v: int, visited: Dict[int, bool]) -> Generator:
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = True
        while 0 < len(queue):
            v = queue.popleft()
            yield v
            for w in g.adjs(v):
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
    
    visited = {k: False for k in g.adj}
    for k in g.adj:
        if not visited[k]:
            yield from _bfs(k, visited)
