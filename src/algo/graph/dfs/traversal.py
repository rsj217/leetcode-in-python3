import unittest

from typing import Generator, Dict
from src.datastruct.adj_list_graph import AdjListGraph
from src.algo.graph import _build_connect_graph, _build_disconnect_graph


def preorder(g: AdjListGraph) -> Generator:
    """ 深度优先搜索前序遍历
    """
    
    def dfs(v: int, visit: Dict[int, bool]) -> Generator:
        visited[v] = True
        yield v
        for w in g.adjs(v):
            if not visited[w]:
                yield from dfs(w, visited)
    
    visited = {k: False for k in g.adj}
    
    for k in g.adj:
        if not visited[k]:
            yield from dfs(k, visited)


def postorder(g: AdjListGraph) -> Generator:
    """ 深度优先搜索后序遍历
    """
    
    def dfs(v: int, visited: Dict[int, bool]) -> Generator:
        visited[v] = True
        for w in g.adjs(v):
            if not visited[w]:
                yield from dfs(w, visited)
        yield v
    
    visited = {k: False for k in g.adj}
    
    for k in g.adj:
        if not visited[k]:
            yield from dfs(k, visited)


def search(g: AdjListGraph) -> Generator:
    def dfs(v: int, visited: Dict[int, bool]) -> Generator:
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
            yield from dfs(k, visit)


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
