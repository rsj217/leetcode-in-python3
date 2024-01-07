import heapq
import unittest
from typing import Dict
from src.datastruct.weight_graph import WeightedGraph


def dijkstra(g: WeightedGraph, s: int) -> (Dict, Dict):
    visited = {v: False for v in range(len(g.graph))}
    dis = {v: float('inf') for v in range(len(g.graph))}
    prev = {v: v for v in range(len(g.graph))}
    prev[s] = s
    dis[s] = 0
    queue = []
    heapq.heappush(queue, (0, s))
    
    while 0 < len(queue):
        weight, v = heapq.heappop(queue)
        if not visited[v]:
            visited[v] = True
            for w, cur_weight in g.graph[v].items():
                if not visited[w]:
                    if dis[v] + cur_weight < dis[w]:
                        dis[w] = dis[v] + cur_weight
                        prev[w] = v
                        heapq.heappush(queue, (dis[w], w))
    return dis, prev


def make_graph():
    s = """6,10
    0,1,5
    0,2,2
    0,5,3
    1,2,20
    1,3,2
    1,4,3
    1,5,1
    2,3,4
    2,4,5
    3,4,1
    """
    return WeightedGraph.loads(s)


class TestDijkstra(unittest.TestCase):

    def setUp(self) -> None:
        self.g = make_graph()
        
    def test_dis(self):
        dis, prev = dijkstra(self.g, 0)
        
        
        