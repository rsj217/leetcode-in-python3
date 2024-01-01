import unittest

from typing import Generator, Dict
from src.datastruct.graph import Graph
from src.algo.graph import _build_connect_graph, _build_disconnect_graph


def preorder(g: Graph) -> Generator:
    """ 深度优先搜索前序遍历
    """
    
    def dfs(v: int, visit: Dict[int, bool]) -> Generator:
        visited[v] = True
        yield v
        for w in g.graph[v]:
            if not visited[w]:
                yield from dfs(w, visited)
    
    visited = {v: False for v in range(len(g.graph))}
    
    for v in range(len(g.graph)):
        if not visited[v]:
            yield from dfs(v, visited)


def postorder(g: Graph) -> Generator:
    """ 深度优先搜索后序遍历
    """
    
    def dfs(v: int, visited: Dict[int, bool]) -> Generator:
        visited[v] = True
        for w in g.graph[v]:
            if not visited[w]:
                yield from dfs(w, visited)
        yield v
    
    visited = {v: False for v in range(len(g.graph))}
    
    for v in range(len(g.graph)):
        if not visited[v]:
            yield from dfs(v, visited)


def search(g: Graph) -> Generator:
    def dfs(v: int, visited: Dict[int, bool]) -> Generator:
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
            yield from dfs(v, visited)


class TestGraphTraversal(unittest.TestCase):
    def setUp(self) -> None:
        self.dg = _build_disconnect_graph()
        self.g = _build_connect_graph()
    
    def test_preorder(self):
        self.assertEqual(list(preorder(self.g)), [0, 1, 3, 2, 6, 5, 4])
        self.assertEqual(list(preorder(self.dg)), [0, 1, 3, 2, 6, 4, 5])
    
    def test_postorder(self):
        self.assertEqual(list(postorder(self.g)), [5, 6, 2, 3, 4, 1, 0])
        self.assertEqual(list(postorder(self.dg)), [6, 2, 3, 4, 1, 0, 5])
    
    def test_search(self):
        self.assertEqual(list(search(self.g)), [0, 2, 6, 5, 3, 1, 4])
        self.assertEqual(list(search(self.dg)), [0, 2, 6, 3, 1, 4, 5])


if __name__ == '__main__':
    unittest.main()
