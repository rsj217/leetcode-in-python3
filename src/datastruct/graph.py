from __future__ import annotations

import unittest
from typing import List
from dataclasses import dataclass, field
import io


@dataclass
class Graph:
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
    
    def degree(self, v: int) -> int:
        return len(self.adj(v))
    
    @classmethod
    def loads(cls, s: str):
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
                assert a not in g._graph[b], "parallel edge"
                g._graph[a].append(b)
                g._graph[b].append(a)
        return g
    
    @classmethod
    def dumps(cls, g: Graph) -> str:
        lines = [f"{g._vsize}, {g._esize}"]
        for idx, item in enumerate(g._graph):
            lines.extend([f"{idx}, {i}" for i in item if idx < i])
        return "\n".join(lines)


class TestAdjListGraphBuild(unittest.TestCase):
    
    def test_connected_graph_loads(self):
        """
        0 ----- 1
        |      / \
        |     /   \
        2 -- 3     4
         \    \
          6 -- 5
        """
        s = """7, 7
            0, 1
            0, 2
            1, 3
            1, 4
            2, 3
            2, 6
            3, 5
            5, 6
        """
        g = Graph.loads(s)
        self.assertEqual(g.vsize, 7)
        self.assertEqual(g.esize, 7)
        
        self.assertEqual(g.graph[0], [1, 2])
        self.assertEqual(g.graph[1], [0, 3, 4])
        self.assertEqual(g.graph[2], [0, 3, 6])
        self.assertEqual(g.graph[3], [1, 2, 5])
        self.assertEqual(g.graph[4], [1])
        self.assertEqual(g.graph[5], [3, 6])
        self.assertEqual(g.graph[6], [2, 5])
    
    def test_connected_graph_dumps(self):
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
        g = Graph.loads(s)
        ans = Graph.dumps(g)
        src = [list(map(int, line.strip().split(","))) for line in io.StringIO(s) if line.strip() != ""]
        des = [list(map(int, line.strip().split(","))) for line in io.StringIO(ans) if line.strip() != ""]
        self.assertListEqual(src, des)
    
    def test_disconnected_graph_loads(self):
        """
        0 ----- 1
        |      / \
        |     /   \
        2 -- 3     4
         \
          6      5
        """
        s = """7, 6
            0, 1
            0, 2
            1, 3
            1, 4
            2, 3
            2, 6
        """
        g = Graph.loads(s)
        self.assertEqual(g.vsize, 7)
        self.assertEqual(g.esize, 6)
        
        self.assertEqual(g.graph[0], [1, 2])
        self.assertEqual(g.graph[1], [0, 3, 4])
        self.assertEqual(g.graph[2], [0, 3, 6])
        self.assertEqual(g.graph[3], [1, 2])
        self.assertEqual(g.graph[4], [1])
        self.assertEqual(g.graph[5], [])
        self.assertEqual(g.graph[6], [2])
    
    def test_disconnected_graph_dumps(self):
        s = """7, 6
            0, 1
            0, 2
            1, 3
            1, 4
            2, 3
            2, 6
        """
        g = Graph.loads(s)
        ans = Graph.dumps(g)
        src = [list(map(int, line.strip().split(","))) for line in io.StringIO(s) if line.strip() != ""]
        des = [list(map(int, line.strip().split(","))) for line in io.StringIO(ans) if line.strip() != ""]
        self.assertListEqual(src, des)


class TestAdjDictGraph(unittest.TestCase):
    
    def setUp(self) -> None:
        """
        0 ----- 1
        |      / \
        |     /   \
        2 -- 3     4
         \
          6      5
        """
        s = """7, 6
            0, 1
            0, 2
            1, 3
            1, 4
            2, 3
            2, 6
        """
        self.g = Graph.loads(s)
    
    def test_has_edge(self):
        self.assertTrue(self.g.has_edge(0, 1))
        self.assertTrue(self.g.has_edge(0, 2))
        self.assertFalse(self.g.has_edge(0, 3))
        self.assertFalse(self.g.has_edge(0, 4))
        self.assertFalse(self.g.has_edge(0, 5))
        self.assertFalse(self.g.has_edge(0, 6))
        
        self.assertTrue(self.g.has_edge(1, 0))
        self.assertFalse(self.g.has_edge(1, 2))
        self.assertTrue(self.g.has_edge(1, 3))
        self.assertTrue(self.g.has_edge(1, 4))
        self.assertFalse(self.g.has_edge(1, 5))
        self.assertFalse(self.g.has_edge(1, 6))
        
        self.assertTrue(self.g.has_edge(2, 0))
        self.assertFalse(self.g.has_edge(2, 1))
        self.assertTrue(self.g.has_edge(2, 3))
        self.assertFalse(self.g.has_edge(2, 4))
        self.assertFalse(self.g.has_edge(2, 5))
        self.assertTrue(self.g.has_edge(2, 6))
        
        self.assertFalse(self.g.has_edge(3, 0))
        self.assertTrue(self.g.has_edge(3, 1))
        self.assertTrue(self.g.has_edge(3, 2))
        self.assertFalse(self.g.has_edge(3, 4))
        self.assertFalse(self.g.has_edge(3, 5))
        self.assertFalse(self.g.has_edge(3, 6))
        
        self.assertFalse(self.g.has_edge(4, 0))
        self.assertTrue(self.g.has_edge(4, 1))
        self.assertFalse(self.g.has_edge(4, 2))
        self.assertFalse(self.g.has_edge(4, 3))
        self.assertFalse(self.g.has_edge(4, 5))
        self.assertFalse(self.g.has_edge(4, 6))
        
        self.assertFalse(self.g.has_edge(5, 0))
        self.assertFalse(self.g.has_edge(5, 1))
        self.assertFalse(self.g.has_edge(5, 2))
        self.assertFalse(self.g.has_edge(5, 3))
        self.assertFalse(self.g.has_edge(5, 4))
        self.assertFalse(self.g.has_edge(5, 6))
        
        self.assertFalse(self.g.has_edge(6, 0))
        self.assertFalse(self.g.has_edge(6, 1))
        self.assertTrue(self.g.has_edge(6, 2))
        self.assertFalse(self.g.has_edge(6, 3))
        self.assertFalse(self.g.has_edge(6, 4))
        self.assertFalse(self.g.has_edge(6, 5))
    
    def test_adjs(self):
        self.assertEqual(self.g.adj(0), [1, 2])
        self.assertEqual(self.g.adj(1), [0, 3, 4])
        self.assertEqual(self.g.adj(2), [0, 3, 6])
        self.assertEqual(self.g.adj(3), [1, 2])
        self.assertEqual(self.g.adj(4), [1])
        self.assertEqual(self.g.adj(5), [])
        self.assertEqual(self.g.adj(6), [2])
    
    def test_degree(self):
        self.assertEqual(self.g.degree(0), 2)
        self.assertEqual(self.g.degree(1), 3)
        self.assertEqual(self.g.degree(2), 3)
        self.assertEqual(self.g.degree(3), 2)
        self.assertEqual(self.g.degree(4), 1)
        self.assertEqual(self.g.degree(5), 0)
        self.assertEqual(self.g.degree(6), 1)


if __name__ == '__main__':
    unittest.main()
