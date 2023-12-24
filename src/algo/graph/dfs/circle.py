import unittest

from typing import Dict
from src.datastruct.adj_list_graph import AdjListGraph
from src.algo.graph import _build_connect_graph, _build_disconnect_graph, _build_without_circle_graph


def has_circle(g: AdjListGraph) -> bool:
    def dfs(v: int, parent: int, visited: Dict[int, bool]) -> bool:
        """ 从 v 出发，找出是否有环
        """
        visited[v] = True
        for w in g.adjs(v):
            if not visited[w]:
                if dfs(w, v, visited):
                    return True
            elif w != parent:
                return True
        return False
    
    visited = {k: False for k in g.adj}
    
    for k in g.adj:
        if not visited[k]:
            if dfs(k, k, visited):
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
