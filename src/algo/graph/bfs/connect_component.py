import unittest
from collections import deque
from typing import Dict, List
from src.datastruct.graph import Graph
from src.algo.graph import _build_connect_graph, _build_disconnect_graph


def connect_component_count(g: Graph) -> int:
    def bfs(v: int, visited: Dict[int, bool]):
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = True
        while 0 < len(queue):
            v = queue.popleft()
            for w in g.graph[v]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
    
    cc_count = 0
    visited = {v: False for v in range(len(g.graph))}
    for v in range(len(g.graph)):
        if not visited[v]:
            cc_count += 1
            bfs(v, visited)
    return cc_count


def connect_component_list(g: Graph) -> List[List[int]]:
    """ 联通量的 vertex 列表
    """
    
    def bfs(v: int, cc_count: int, visited: Dict[int, int]):
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = cc_count
        
        while 0 < len(queue):
            v = queue.popleft()
            for w in g.graph[v]:
                if visited[w] == 0:
                    queue.append(w)
                    visited[w] = cc_count
    
    cc_count = 0
    visited = {v: 0 for v in range(len(g.graph))}
    for v in range(len(g.graph)):
        if visited[v] == 0:
            cc_count += 1
            bfs(v, cc_count, visited)
    
    ans = [[] for _ in range(cc_count)]
    for k, v in visited.items():
        ans[v - 1].append(k)
    return ans


def is_connected(g: Graph, s: int, t: int) -> bool:
    """ 两个 vertext 是否联通
    """
    
    def bfs(v: int, cc_count: int, visited: Dict[int, int]):
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = cc_count
        
        while 0 < len(queue):
            v = queue.popleft()
            for w in g.graph[v]:
                if visited[w] == 0:
                    queue.append(w)
                    visited[w] = cc_count
    
    assert 0 <= s, "vertex invalid"
    assert 0 <= t, "vertex invalid"
    
    cc_count = 0
    visited = {v: 0 for v in range(len(g.graph))}
    for v in range(len(g.graph)):
        if visited[v] == 0:
            cc_count += 1
            bfs(v, cc_count, visited)
    
    return visited[s] == visited[t]


class TestGraphConnectComponent(unittest.TestCase):
    def setUp(self) -> None:
        self.dg = _build_disconnect_graph()
        self.g = _build_connect_graph()
    
    def test_connect_component_count(self):
        self.assertEqual(connect_component_count(self.g), 1)
        self.assertEqual(connect_component_count(self.dg), 2)
    
    def test_connect_component_list(self):
        ans = connect_component_list(self.g)
        # self.assertEqual(1, len(ans))
        self.assertEqual(ans[0], [0, 1, 2, 3, 4, 5, 6])
        
        ans = connect_component_list(self.dg)
        self.assertEqual(2, len(ans))
        self.assertEqual(ans[0], [0, 1, 2, 3, 4, 6])
        self.assertEqual(ans[1], [5])
    
    def test_is_connect(self):
        for v in range(len(self.g.graph)):
            for w in range(len(self.g.graph)):
                self.assertTrue(is_connected(self.g, v, w))
        
        self.assertTrue(is_connected(self.dg, 0, 1))
        self.assertTrue(is_connected(self.dg, 0, 2))
        self.assertTrue(is_connected(self.dg, 0, 3))
        self.assertTrue(is_connected(self.dg, 0, 4))
        self.assertFalse(is_connected(self.dg, 0, 5))
        self.assertTrue(is_connected(self.dg, 0, 6))
        
        self.assertTrue(is_connected(self.dg, 1, 0))
        self.assertTrue(is_connected(self.dg, 1, 2))
        self.assertTrue(is_connected(self.dg, 1, 3))
        self.assertTrue(is_connected(self.dg, 1, 4))
        self.assertFalse(is_connected(self.dg, 1, 5))
        self.assertTrue(is_connected(self.dg, 1, 6))
        
        self.assertTrue(is_connected(self.dg, 2, 0))
        self.assertTrue(is_connected(self.dg, 2, 1))
        self.assertTrue(is_connected(self.dg, 2, 3))
        self.assertTrue(is_connected(self.dg, 2, 4))
        self.assertFalse(is_connected(self.dg, 2, 5))
        self.assertTrue(is_connected(self.dg, 2, 6))
        
        self.assertTrue(is_connected(self.dg, 3, 0))
        self.assertTrue(is_connected(self.dg, 3, 1))
        self.assertTrue(is_connected(self.dg, 3, 2))
        self.assertTrue(is_connected(self.dg, 3, 4))
        self.assertFalse(is_connected(self.dg, 3, 5))
        self.assertTrue(is_connected(self.dg, 3, 6))
        
        self.assertTrue(is_connected(self.dg, 4, 0))
        self.assertTrue(is_connected(self.dg, 4, 1))
        self.assertTrue(is_connected(self.dg, 4, 2))
        self.assertTrue(is_connected(self.dg, 4, 3))
        self.assertFalse(is_connected(self.dg, 4, 5))
        self.assertTrue(is_connected(self.dg, 4, 6))
        
        self.assertFalse(is_connected(self.dg, 5, 0))
        self.assertFalse(is_connected(self.dg, 5, 1))
        self.assertFalse(is_connected(self.dg, 5, 2))
        self.assertFalse(is_connected(self.dg, 5, 3))
        self.assertFalse(is_connected(self.dg, 5, 4))
        self.assertFalse(is_connected(self.dg, 5, 6))
        
        self.assertTrue(is_connected(self.dg, 6, 0))
        self.assertTrue(is_connected(self.dg, 6, 1))
        self.assertTrue(is_connected(self.dg, 6, 2))
        self.assertTrue(is_connected(self.dg, 6, 3))
        self.assertTrue(is_connected(self.dg, 6, 4))
        self.assertFalse(is_connected(self.dg, 6, 5))


if __name__ == '__main__':
    unittest.main()
