import unittest

from collections import deque
from typing import Generator, Dict
from src.datastruct.adj_list_graph import AdjListGraph
from src.algo.graph import _build_connect_graph, _build_disconnect_graph


def bfsorder(g: AdjListGraph) -> Generator:
    def bfs(v: int, visited: Dict[int, bool]) -> Generator:
        queue = deque(maxlen=g.vsize)
        queue.append(v)
        visited[v] = True
        while 0 < len(queue):
            v = queue.popleft()
            yield v
            for w in g.adjs(v):
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
    
    visited = {k: False for k in g.adj}
    for k in g.adj:
        if not visited[k]:
            yield from bfs(k, visited)


class TestGraphTraversal(unittest.TestCase):
    def setUp(self) -> None:
        self.dg = _build_disconnect_graph()
        self.g = _build_connect_graph()
    
    def test_bfsorder(self):
        self.assertEqual(list(bfsorder(self.g)), [0, 1, 2, 3, 4, 6, 5])
        self.assertEqual(list(bfsorder(self.dg)), [0, 1, 2, 3, 4, 6, 5])


if __name__ == '__main__':
    unittest.main()
