from __future__ import annotations

import unittest
from typing import List
from dataclasses import dataclass, field
import io


@dataclass
class DiGraph:
    """ Graph 表示使用领接表实现的无向无权图
    """
    _vsize: int = 0
    _esize: int = 0
    _graph: List[List[int]] = field(default_factory=list)
    
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
        return self._graph[v]
    
    @classmethod
    def loads(cls, s: str) -> DiGraph:
        g = cls()
        text = io.StringIO(s)
        first_line = next(text)
        v, e = map(int, first_line.strip().split(","))
        assert 0 < v, "invalid vertex"
        
        g._vsize, g._esize = v, e
        g._graph = [[] for _ in range(v)]
        
        for line in text:
            line = line.strip()
            if line != "":
                a, b = map(int, line.split(","))
                assert a != b, "self loop edge err"
                assert b not in g._graph[a], "parallel edge"
                g._graph[a].append(b)
        return g
    
    @classmethod
    def dumps(cls, g: DiGraph) -> str:
        lines = [f"{g._vsize}, {g._esize}"]
        for idx, item in enumerate(g._graph):
            lines.extend([f"{idx}, {i}" for i in item])
        return "\n".join(lines)


class TestAdjListGraphBuild(unittest.TestCase):
    
    def test_disgraph_loads(self):
        """
              0
            /  \
          /     \
        1 -------2
         \     / |
          \  /   |
          3 -----4
        """
        s = """5, 8
            0, 1
            1, 2
            1, 3
            2, 0
            2, 4
            3, 1
            3, 2
            4, 3
        """
        g = DiGraph.loads(s)
        self.assertEqual(g.vsize, 5)
        self.assertEqual(g.esize, 8)
        
        self.assertEqual(g.graph[0], [1])
        self.assertEqual(g.graph[1], [2, 3])
        self.assertEqual(g.graph[2], [0, 4])
        self.assertEqual(g.graph[3], [1, 2])
        self.assertEqual(g.graph[4], [3])
    
    def test_disgraph_dumps(self):
        s = """5, 8
            0, 1
            1, 2
            1, 3
            2, 0
            2, 4
            3, 1
            3, 2
            4, 3
        """
        g = DiGraph.loads(s)
        ans = DiGraph.dumps(g)
        src = [list(map(int, line.strip().split(","))) for line in io.StringIO(s) if line.strip() != ""]
        des = [list(map(int, line.strip().split(","))) for line in io.StringIO(ans) if line.strip() != ""]
        self.assertListEqual(src, des)


if __name__ == '__main__':
    unittest.main()
