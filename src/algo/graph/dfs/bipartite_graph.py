import unittest

from typing import Dict, List
from src.datastruct.graph import Graph
from src.algo.graph import _build_bipartite_graph, _build_unbipartite_graph


def is_bipartite(g: Graph) -> bool:
    def dfs(v: int, color: int, colors: Dict[int, int], visited: Dict[int, bool]) -> bool:
        visited[v] = True
        colors[v] = color
        for w in g.graph[v]:
            if not visited[w]:
                if not dfs(w, 0 - color, colors, visited):
                    return False
            elif colors[v] == colors[w]:
                return False
        return True
    
    visited = {v: False for v in range(len(g.graph))}
    colors = {v: 0 for v in range(len(g.graph))}
    for v in range(len(g.graph)):
        if not visited[v]:
            if not dfs(v, 1, colors, visited):
                return False
    return True


def bipartite_list(g: Graph) -> List[List[int]]:
    def dfs(v: int, color: int, colors: Dict[int, int], visited: Dict[int, bool]):
        visited[v] = True
        colors[v] = color
        for w in g.graph[v]:
            if not visited[w]:
                if not dfs(w, 0 - color, colors, visited):
                    return False
            elif colors[v] == colors[w]:
                return False
        return True
    
    visited = {v: False for v in range(len(g.graph))}
    colors = {v: 0 for v in range(len(g.graph))}
    
    is_bipart = True
    for v in range(len(g.graph)):
        if not visited[v]:
            if not dfs(v, 1, colors, visited):
                return []
    
    if not is_bipart:
        return []
    ans = [[] for _ in range(2)]
    for c in colors:
        if colors[c] == -1:
            ans[0].append(c)
        else:
            ans[1].append(c)
    return ans


class TestBapartiteGraph(unittest.TestCase):
    
    def setUp(self) -> None:
        self.bipartitle_g = _build_bipartite_graph()
        self.unbipartitle_g = _build_unbipartite_graph()
    
    def test_is_bipartite(self):
        self.assertTrue(is_bipartite(self.bipartitle_g))
        self.assertFalse(is_bipartite(self.unbipartitle_g))
    
    def test_bipartite_list(self):
        self.assertEqual([], bipartite_list(self.unbipartitle_g))
        self.assertEqual([[1, 2, 5], [0, 3, 4, 6]], bipartite_list(self.bipartitle_g))


if __name__ == '__main__':
    unittest.main()
