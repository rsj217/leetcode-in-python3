import unittest

from typing import Dict, List
from src.datastruct.adj_list_graph import AdjListGraph
from src.algo.graph import _build_connect_graph, _build_disconnect_graph


def single_source_path(g: AdjListGraph, s: int, t: int) -> List[int]:
    def dfs(v: int, parent, prev: Dict[int, int], visited: Dict[int, bool]):
        visited[v] = True
        prev[v] = parent
        for w in g.adjs(v):
            if not visited[w]:
                dfs(w, v, prev, visited)
    
    visited = {k: False for k in g.adj}
    prev = {k: k for k in g.adj}
    dfs(s, s, prev, visited)
    
    ans = []
    if not visited[t]:
        return ans
    
    curr = t
    while curr != s:
        ans.append(curr)
        curr = prev[curr]
    ans.append(s)
    ans.reverse()
    return ans


def path(g: AdjListGraph, s: int, t: int) -> List[int]:
    """ 从 s 到 t 的路径，找到后提前终止遍历
    """
    
    def dfs(v: int, parent: int, prev: Dict[int, int], visited: Dict[int, bool]) -> bool:
        visited[v] = True
        prev[v] = parent
        if v == t:
            return True
        for w in g.adjs(v):
            if not visited[w]:
                if dfs(w, v, prev, visited):
                    return True
        return False
    
    assert 0 <= s, "vertex invalid"
    assert 0 <= t, "vertex invalid"
    
    visited = {k: False for k in g.adj}
    prev = {k: k for k in g.adj}
    is_find = dfs(s, s, prev, visited)
    ans = []
    if not is_find:
        return ans
    
    curr = t
    while curr != s:
        ans.append(curr)
        curr = prev[curr]
    ans.append(s)
    ans.reverse()
    return ans


class TestSingleSourcePath(unittest.TestCase):
    
    def setUp(self) -> None:
        self.dg = _build_disconnect_graph()
        self.g = _build_connect_graph()
    
    def test_single_source_path(self):
        self.assertEqual(single_source_path(self.g, 0, 1), [0, 1])
        self.assertEqual(single_source_path(self.g, 0, 2), [0, 1, 3, 2])
        self.assertEqual(single_source_path(self.g, 0, 3), [0, 1, 3])
        self.assertEqual(single_source_path(self.g, 0, 4), [0, 1, 4])
        self.assertEqual(single_source_path(self.g, 0, 5), [0, 1, 3, 2, 6, 5])
        self.assertEqual(single_source_path(self.g, 0, 6), [0, 1, 3, 2, 6])
        
        self.assertEqual(single_source_path(self.dg, 0, 1), [0, 1])
        self.assertEqual(single_source_path(self.dg, 0, 2), [0, 1, 3, 2])
        self.assertEqual(single_source_path(self.dg, 0, 3), [0, 1, 3])
        self.assertEqual(single_source_path(self.dg, 0, 4), [0, 1, 4])
        self.assertEqual(single_source_path(self.dg, 0, 5), [])
        self.assertEqual(single_source_path(self.dg, 0, 6), [0, 1, 3, 2, 6])
    
    def test_path(self):
        self.assertEqual(path(self.g, 0, 1), [0, 1])
        self.assertEqual(path(self.g, 0, 2), [0, 1, 3, 2])
        self.assertEqual(path(self.g, 0, 3), [0, 1, 3])
        self.assertEqual(path(self.g, 0, 4), [0, 1, 4])
        self.assertEqual(path(self.g, 0, 5), [0, 1, 3, 2, 6, 5])
        self.assertEqual(path(self.g, 0, 6), [0, 1, 3, 2, 6])
        
        self.assertEqual(path(self.dg, 0, 1), [0, 1])
        self.assertEqual(path(self.dg, 0, 2), [0, 1, 3, 2])
        self.assertEqual(path(self.dg, 0, 3), [0, 1, 3])
        self.assertEqual(path(self.dg, 0, 4), [0, 1, 4])
        self.assertEqual(path(self.dg, 0, 5), [])
        self.assertEqual(path(self.dg, 0, 6), [0, 1, 3, 2, 6])


if __name__ == '__main__':
    unittest.main()
