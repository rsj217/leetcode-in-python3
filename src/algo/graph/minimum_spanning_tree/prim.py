import heapq
import unittest
from src.algo.graph import _build_weighted_graph

from src.datastruct.weight_graph import WeightedGraph


def prim(g: WeightedGraph):
    """
    graph: 图的邻接表表示，[顶点: {邻接顶点, 边的权重}, ...]
    :return: 返回最小生成树的边
    """
    visited = {v: False for v in range(len(g.graph))}
    
    visited[0] = True
    queue = [(v, 0, k) for k, v in g.graph[0].items()]
    heapq.heapify(queue)
    
    mst = []
    while 0 < len(queue):
        weight, s, t = heapq.heappop(queue)
        if not visited[t]:
            mst.append((s, t, weight))
            visited[t] = True
            
            for k, v in g.graph[t].items():
                if not visited[k]:
                    heapq.heappush(queue, (v, t, k))
    return mst


class TestPrim(unittest.TestCase):
    def setUp(self) -> None:
        self.g = _build_weighted_graph()
    
    def test_prim(self):
        ans = prim(self.g)
        self.assertEqual(ans[0], (0, 1, 2))
        self.assertEqual(ans[1], (1, 2, 1))
        self.assertEqual(ans[2], (0, 5, 2))
        self.assertEqual(ans[3], (1, 4, 3))
        self.assertEqual(ans[4], (4, 3, 1))
        self.assertEqual(ans[5], (3, 6, 5))


if __name__ == '__main__':
    unittest.main()
