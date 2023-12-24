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


def preorder_dfs(g: AdjListGraph):
    visit = {k: False for k, _ in g._adj.items()}
    
    def _dfs(v: int):
        if visit[v]:
            return
        visit[v] = True
        # 先序
        yield v
        for w in g.adjs(v):
            yield from _dfs(w)
    
    # 每一个点都遍历，保证非连通图覆盖
    for k, _ in g.adj.items():
        yield from _dfs(k)


def postorder_dfs(g: AdjListGraph):
    visit = {k: False for k, _ in g._adj.items()}
    
    def _dfs(v: int):
        if visit[v]:
            return
        visit[v] = True
        for w in g.adjs(v):
            yield from _dfs(w)
        yield v
    
    # 每一个点都遍历，保证非连通图覆盖
    for k, _ in g.adj.items():
        yield from _dfs(k)


class TestAdjListGraphBuild(unittest.TestCase):
    
    def test_connected_graph_loads(self):
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
        self.assertEqual(g.vsize, 7)
        self.assertEqual(g.esize, 9)
        
        self.assertEqual(g.adj[0], [1, 3])
        self.assertEqual(g.adj[1], [0, 2, 6])
        self.assertEqual(g.adj[2], [1, 3, 5])
        self.assertEqual(g.adj[3], [0, 2, 4])
        self.assertEqual(g.adj[4], [3, 5])
        self.assertEqual(g.adj[5], [2, 4, 6])
        self.assertEqual(g.adj[6], [1, 5])
    
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
        g = AdjListGraph.load(s)
        ans = AdjListGraph.dumps(g)
        src = [list(map(int, line.strip().split(","))) for line in io.StringIO(s) if line.strip() != ""]
        des = [list(map(int, line.strip().split(","))) for line in io.StringIO(ans) if line.strip() != ""]
        self.assertListEqual(src, des)
    
    def test_disconnected_graph_loads(self):
        s = """7, 6
            0, 1
            0, 2
            1, 3
            1, 4
            2, 3
            2, 6
        """
        g = AdjListGraph.load(s)
        self.assertEqual(g.vsize, 7)
        self.assertEqual(g.esize, 6)
        
        self.assertEqual(g.adj[0], [1, 2])
        self.assertEqual(g.adj[1], [0, 3, 4])
        self.assertEqual(g.adj[2], [0, 3, 6])
        self.assertEqual(g.adj[3], [1, 2])
        self.assertEqual(g.adj[4], [1])
        self.assertEqual(g.adj[5], [])
        self.assertEqual(g.adj[6], [2])
    
    def test_disconnected_graph_dumps(self):
        s = """7, 6
            0, 1
            0, 2
            1, 3
            1, 4
            2, 3
            2, 6
        """
        g = AdjListGraph.load(s)
        ans = AdjListGraph.dumps(g)
        src = [list(map(int, line.strip().split(","))) for line in io.StringIO(s) if line.strip() != ""]
        des = [list(map(int, line.strip().split(","))) for line in io.StringIO(ans) if line.strip() != ""]
        self.assertListEqual(src, des)


class TestAdjDictGraph(unittest.TestCase):
    
    def setUp(self) -> None:
        s = """7, 6
            0, 1
            0, 2
            1, 3
            1, 4
            2, 3
            2, 6
        """
        self.g = AdjListGraph.load(s)
    
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
        self.assertEqual(self.g.adjs(0), [1, 2])
        self.assertEqual(self.g.adjs(1), [0, 3, 4])
        self.assertEqual(self.g.adjs(2), [0, 3, 6])
        self.assertEqual(self.g.adjs(3), [1, 2])
        self.assertEqual(self.g.adjs(4), [1])
        self.assertEqual(self.g.adjs(5), [])
        self.assertEqual(self.g.adjs(6), [2])
    
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
