import unittest

from typing import Dict
from src.datastruct.adj_list_graph import AdjListGraph
from src.algo.graph.dfs import _build_disconnect_graph, _build_bipartite_graph, _build_unbipartite_graph


def is_bipartite(g: AdjListGraph) -> bool:
    def dfs(v: int, color: int, colors: Dict[int, int], visited: Dict[int, bool]):
        
        visited[v] = True
        colors[v] = color
        for w in g.adjs(v):
            if not visited[w]:
                if not dfs(w, 0 - color, colors, visited):
                    return False
            elif colors[v] == colors[w]:
                return False
        return True
    
    visited = {k: False for k in g.adj}
    colors = {k: 0 for k in g.adj}
    for k in g.adj:
        if not visited[k]:
            if not dfs(k, 1, colors, visited):
                return False
    return True


class TestBapartiteGraph(unittest.TestCase):
    
    def setUp(self) -> None:
        self.bipartitle_g = _build_bipartite_graph()
        self.unbipartitle_g = _build_unbipartite_graph()
    
    def test_is_bipartite(self):
        self.assertTrue(is_bipartite(self.bipartitle_g))
        self.assertFalse(is_bipartite(self.unbipartitle_g))


if __name__ == '__main__':
    unittest.main()
