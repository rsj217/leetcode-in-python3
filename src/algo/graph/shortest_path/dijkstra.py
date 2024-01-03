import heapq
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
