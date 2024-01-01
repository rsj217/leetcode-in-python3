import unittest

from collections import deque
from typing import Generator, Dict
from src.datastruct.graph import Graph
from src.algo.graph import _build_connect_graph, _build_disconnect_graph


def bfsorder(g: Graph) -> Generator:
    def bfs(v: int, visited: Dict[int, bool]) -> Generator:
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = True
        while 0 < len(queue):
            v = queue.popleft()
            yield v
            for w in g.adj(v):
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
    
    visited = {v: False for v in range(len(g.graph))}
    for v in range(len(g.graph)):
        if not visited[v]:
            yield from bfs(v, visited)


def levelorder(g: Graph) -> Generator:
    def bfs(v: int, visited: Dict[int, bool]) -> Generator:
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = True
        while 0 < len(queue):
            lsize = len(queue)
            level = []
            for _ in range(lsize):
                v = queue.popleft()
                level.append(v)
                for w in g.adj(v):
                    if not visited[w]:
                        queue.append(w)
                        visited[w] = True
            yield level
    
    visited = {v: False for v in range(len(g.graph))}
    for v in range(len(g.graph)):
        if not visited[v]:
            yield from bfs(v, visited)


def disorder(g: Graph, s: int, t: int) -> int:
    def bfs(v: int, dis: Dict[int, int], visited: Dict[int, bool]):
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = True
        
        while 0 < len(queue):
            v = queue.popleft()
            for w in g.adj(v):
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
                    dis[w] = dis[v] + 1
    
    assert 0 <= s, "vertex invalid"
    visited = {v: False for v in range(len(g.graph))}
    dis = {v: 0 for v in range(len(g.graph))}
    bfs(s, dis, visited)
    if not visited[t]:
        return -1
    return dis[t]


class TestGraphTraversal(unittest.TestCase):
    def setUp(self) -> None:
        self.dg = _build_disconnect_graph()
        self.g = _build_connect_graph()
    
    def test_bfsorder(self):
        self.assertEqual(list(bfsorder(self.g)), [0, 1, 2, 3, 4, 6, 5])
        self.assertEqual(list(bfsorder(self.dg)), [0, 1, 2, 3, 4, 6, 5])
    
    def test_levelorder(self):
        self.assertEqual(list(levelorder(self.g)), [
            [0],
            [1, 2],
            [3, 4, 6],
            [5]])
        self.assertEqual(list(levelorder(self.dg)), [
            [0],
            [1, 2],
            [3, 4, 6],
            [5]
        ])
    
    def test_disorder(self):
        self.assertEqual(disorder(self.g, 0, 0), 0)
        self.assertEqual(disorder(self.g, 0, 1), 1)
        self.assertEqual(disorder(self.g, 0, 2), 1)
        self.assertEqual(disorder(self.g, 0, 3), 2)
        self.assertEqual(disorder(self.g, 0, 4), 2)
        self.assertEqual(disorder(self.g, 0, 5), 3)
        self.assertEqual(disorder(self.g, 0, 6), 2)
        
        self.assertEqual(disorder(self.dg, 0, 0), 0)
        self.assertEqual(disorder(self.dg, 0, 1), 1)
        self.assertEqual(disorder(self.dg, 0, 2), 1)
        self.assertEqual(disorder(self.dg, 0, 3), 2)
        self.assertEqual(disorder(self.dg, 0, 4), 2)
        self.assertEqual(disorder(self.dg, 0, 5), -1)
        self.assertEqual(disorder(self.dg, 0, 6), 2)


if __name__ == '__main__':
    unittest.main()
