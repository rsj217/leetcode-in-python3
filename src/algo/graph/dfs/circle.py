import unittest

from typing import Dict
from src.datastruct.graph import Graph
from src.algo.graph import _build_connect_graph, _build_disconnect_graph, _build_without_circle_graph


def has_circle(g: Graph) -> bool:
    def dfs(v: int, parent: int, visited: Dict[int, bool]) -> bool:
        """ 从 v 出发，找出是否有环
        """
        visited[v] = True
        for w in g.adj(v):
            if not visited[w]:
                if dfs(w, v, visited):
                    return True
            elif w != parent:
                return True
        return False
    
    visited = {v: False for v in range(len(g.graph))}
    
    for v in range(len(g.graph)):
        if not visited[v]:
            if dfs(v, v, visited):
                return True
    return False


class TestCircle(unittest.TestCase):
    
    def setUp(self) -> None:
        self.dg = _build_disconnect_graph()
        self.g = _build_connect_graph()
        self.without_circle_g = _build_without_circle_graph()
    
    def test_has_circle(self):
        self.assertTrue(has_circle(self.g))
        self.assertTrue(has_circle(self.dg))
        self.assertFalse(has_circle(self.without_circle_g))


if __name__ == '__main__':
    unittest.main()
