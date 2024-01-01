from collections import deque
import unittest

from typing import Dict, List
from src.datastruct.graph import Graph
from src.algo.graph import _build_connect_graph, _build_disconnect_graph


def single_source_path(g: Graph, s: int, t: int) -> List[int]:
    def bfs(v: int, parent: int, prev: Dict[int, int], visited: Dict[int, int]):
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = True
        prev[v] = parent
        
        while 0 < len(queue):
            v = queue.popleft()
            for w in g.graph[v]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
                    prev[w] = v
    
    visited = {v: False for v in range(len(g.graph))}
    prev = {v: v for v in range(len(g.graph))}
    
    bfs(s, s, prev, visited)
    
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


def path(g: Graph, s: int, t: int) -> List[int]:
    """ 从 s 到 t 的路径，找到后提前终止遍历
    """
    
    def bfs(v: int, parent: int, prev: Dict[int, int], visited: Dict[int, bool]) -> bool:
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = True
        
        while 0 < len(queue):
            v = queue.popleft()
            if v == t:
                return True
            for w in g.graph[v]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
                    prev[w] = v
        
        return False
    
    assert 0 <= s, "vertex invalid"
    assert 0 <= t, "vertex invalid"
    
    visited = {v: False for v in range(len(g.graph))}
    prev = {v: v for v in range(len(g.graph))}
    
    is_find = bfs(s, s, prev, visited)
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
        self.assertEqual(single_source_path(self.g, 0, 2), [0, 2])
        self.assertEqual(single_source_path(self.g, 0, 3), [0, 1, 3])
        self.assertEqual(single_source_path(self.g, 0, 4), [0, 1, 4])
        self.assertEqual(single_source_path(self.g, 0, 5), [0, 1, 3, 5])
        self.assertEqual(single_source_path(self.g, 0, 6), [0, 2, 6])
        
        self.assertEqual(single_source_path(self.dg, 0, 1), [0, 1])
        self.assertEqual(single_source_path(self.dg, 0, 2), [0, 2])
        self.assertEqual(single_source_path(self.dg, 0, 3), [0, 1, 3])
        self.assertEqual(single_source_path(self.dg, 0, 4), [0, 1, 4])
        self.assertEqual(single_source_path(self.dg, 0, 5), [])
        self.assertEqual(single_source_path(self.dg, 0, 6), [0, 2, 6])
    
    def test_path(self):
        self.assertEqual(single_source_path(self.g, 0, 1), [0, 1])
        self.assertEqual(single_source_path(self.g, 0, 2), [0, 2])
        self.assertEqual(single_source_path(self.g, 0, 3), [0, 1, 3])
        self.assertEqual(single_source_path(self.g, 0, 4), [0, 1, 4])
        self.assertEqual(single_source_path(self.g, 0, 5), [0, 1, 3, 5])
        self.assertEqual(single_source_path(self.g, 0, 6), [0, 2, 6])
        
        self.assertEqual(single_source_path(self.dg, 0, 1), [0, 1])
        self.assertEqual(single_source_path(self.dg, 0, 2), [0, 2])
        self.assertEqual(single_source_path(self.dg, 0, 3), [0, 1, 3])
        self.assertEqual(single_source_path(self.dg, 0, 4), [0, 1, 4])
        self.assertEqual(single_source_path(self.dg, 0, 5), [])
        self.assertEqual(single_source_path(self.dg, 0, 6), [0, 2, 6])


if __name__ == '__main__':
    unittest.main()
