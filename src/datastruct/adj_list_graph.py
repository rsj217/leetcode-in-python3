from __future__ import annotations

import unittest
from typing import List, Dict
from dataclasses import dataclass, field
import io


@dataclass
class AdjListGraph:
    _vsize: int = 0
    _esize: int = 0
    _adj: Dict[int, List[int]] = field(default_factory=dict)
    
    @property
    def vsize(self):
        return self._vsize
    
    @property
    def esize(self):
        return self._esize
    
    @property
    def adj(self):
        return self._adj
    
    def __str__(self) -> str:
        lines = [f"{k}: {v}" for k, v in self._adj.items()]
        return "\n".join(lines)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def has_edge(self, v: int, w: int) -> bool:
        return w in self._adj[v]
    
    def adjs(self, v: int) -> List[int]:
        assert 0 <= v, "invalid vertex"
        return self._adj[v]
    
    def degree(self, v: int) -> int:
        return len(self.adjs(v))
    
    @classmethod
    def load(cls, s: str):
        g = cls()
        text = io.StringIO(s)
        first_line = next(text)
        v, e = map(int, first_line.strip().split(","))
        assert 0 < v, "invalid vertex"
        
        g._vsize, g._esize = v, e
        g._adj = {i: [] for i in range(v)}
        
        for line in text:
            line = line.strip()
            if line != "":
                a, b = map(int, line.split(","))
                assert a != b, "self loop edge err"
                assert b not in g._adj[a], "parallel edge"
                assert a not in g._adj[b], "parallel edge"
                g._adj[a].append(b)
                g._adj[b].append(a)
        return g
    
    @classmethod
    def dumps(cls, g: AdjListGraph) -> str:
        lines = [f"{g._vsize}, {g._esize}"]
        for k, v in g._adj.items():
            lines.extend([f"{k}, {i}" for i in v if k < i])
        return "\n".join(lines)


def travel(g: AdjListGraph):
    visit = {k: False for k, _ in g._adj.items()}
    
    def dfs(v: int):
        if visit[v]:
            return
        visit[v] = True
        yield v
        for w in g.adjs(v):
            yield from dfs(w)
    
    yield from dfs(0)


class TestAdjDictGraph(unittest.TestCase):
    
    def setUp(self) -> None:
        s = """7, 9
            0, 1
            0, 3
            1, 2
            1, 6
            2, 3
            2, 5
            3, 4
            4, 5
            5, 6                                                                               
        """
        self.g = AdjListGraph.load(s)
        print(self.g)


if __name__ == '__main__':
    # unittest.main()
    s = """7, 9
        0, 1
        0, 3
        1, 2
        1, 6
        2, 3
        2, 5
        3, 4
        4, 5
        5, 6                                                                               
    """
    
    g = AdjListGraph.load(s)
    # print(g)
    
    ans = AdjListGraph.dumps(g)
    print(ans)
    import pprint
    
    pprint.pprint(g.adj)
    
    ans = list(travel(g))
    print(ans)
