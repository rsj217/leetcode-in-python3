from __future__ import annotations

import io
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class WeightedGraph:
    """ 使用领接表实现的带权无向图
    """
    _vsize: int = 0
    _esize: int = 0
    _graph: List[Dict[int, int]] = field(default_factory=list)
    
    @property
    def vsize(self):
        return self._vsize
    
    @property
    def esize(self):
        return self._esize
    
    @property
    def graph(self):
        return self._graph
    
    def __str__(self) -> str:
        lines = [f"{idx}: {item}" for idx, item in enumerate(self._graph)]
        return "\n".join(lines)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def has_edge(self, v: int, w: int) -> bool:
        return w in self._graph[v]
    
    def adj(self, v: int) -> List[int]:
        """ 获取vertex v 的领接顶点列表 """
        assert 0 <= v, "invalid vertex"
        return list(self._graph[v].keys())
    
    def degree(self, v: int) -> int:
        return len(self.adj(v))
    
    @classmethod
    def loads(cls, s: str) -> WeightedGraph:
        g = cls()
        text = io.StringIO(s)
        first_line = next(text)
        v, e = map(int, first_line.strip().split(","))
        assert 0 < v, "invalid vertex"
        
        g._vsize, g._esize = v, e
        g._graph = [{} for _ in range(v)]
        
        for line in text:
            line = line.strip()
            if line != "":
                a, b, w = map(int, line.split(","))
                assert a != b, "self loop edge err"
                assert b not in g._graph[a], "parallel edge"
                assert a not in g._graph[b], "parallel edge"
                g._graph[a][b] = w
                g._graph[b][a] = w
        return g
    
    @classmethod
    def dumps(cls, g: WeightedGraph) -> str:
        lines = [f"{g._vsize}, {g._esize}"]
        for idx, item in enumerate(g._graph):
            lines.extend([f"{idx}, {k}, {v}" for k, v in item.items() if idx < k])
        return "\n".join(lines)


if __name__ == '__main__':
    s = """7,12
    0,1,2
    0,3,7
    0,5,2
    1,2,1
    1,3,4
    1,4,3
    1,5,5
    2,4,4
    2,5,4
    3,4,1
    3,6,5
    4,6,7
    """
    g = WeightedGraph.loads(s)
    print(g)
