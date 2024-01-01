from typing import Dict, Generator
from collections import deque
from src.datastruct.graph import Graph
from src.datastruct import graphviz


def _build_disconnect_graph() -> Graph:
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
    
    return Graph.loads(s)


def _build_connect_graph() -> Graph:
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
    return Graph.loads(s)


def _build_without_circle_graph() -> Graph:
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
    return Graph.loads(s)


def _build_bipartite_graph() -> Graph:
    s = """7,7
    0, 1
    0, 2
    1, 3
    1, 4
    2, 3
    2, 6
    5, 6
    """
    return Graph.loads(s)


def _build_unbipartite_graph() -> Graph:
    s = """4, 6
    0, 1
    0, 2
    0, 3
    1, 2
    1, 3
    2, 3
    """
    return Graph.loads(s)


def show_disconnect_graph(g: Graph):
    print(g)
    graphviz.graph(g)


def dfs(g: Graph) -> Generator:
    def _dfs(v: int, visited: Dict[int, bool]) -> Generator:
        stack = [v]
        visited[v] = True
        while 0 < len(stack):
            v = stack.pop()
            yield v
            for w in g.graph[v]:
                if not visited[w]:
                    stack.append(w)
                    visited[w] = True
    
    visited = {v: False for v in range(len(g.graph))}
    for v in range(len(g.graph)):
        if not visited[v]:
            yield from _dfs(v, visited)


def bfs(g: Graph) -> Generator:
    def _bfs(v: int, visited: Dict[int, bool]) -> Generator:
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = True
        while 0 < len(queue):
            v = queue.popleft()
            yield v
            for w in g.graph[v]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
    
    visited = {v: False for v in range(len(g.graph))}
    for v in range(len(g.graph)):
        if not visited[v]:
            yield from _bfs(v, visited)
