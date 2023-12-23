from __future__ import annotations

import unittest
from typing import List
from dataclasses import dataclass, field
import io


@dataclass
class AdjMatrixGraph:
    _vsize: int = 0
    _esize: int = 0
    _adj: List[List[int]] = field(default_factory=list)
    
    @property
    def vsize(self) -> int:
        return self._vsize
    
    @property
    def esize(self) -> int:
        return self._esize
    
    @property
    def adj(self):
        return self._adj
    
    def __str__(self):
        title = [str(i) for i in range(self._vsize)]
        title.insert(0, "  ")
        ans = [" ".join(title)]
        for idx, row in enumerate(self._adj):
            newRow = row.copy()
            newRow.insert(0, f"{idx}:")
            ans.append(" ".join(map(str, newRow)))
        return "\n".join(ans)
    
    def __repr__(self):
        return self.__str__()
    
    def has_edge(self, v: int, w: int) -> bool:
        assert 0 <= v or 0 <= w, "invalid vertex"
        return self._adj[v][w] == 1
    
    def adjs(self, v: int) -> List[int]:
        assert 0 <= v, "invalid vertex"
        return [i for i in range(self._vsize) if self._adj[v][i] == 1]
    
    def degree(self, v: int) -> int:
        return len(self.adjs(v))
    
    @classmethod
    def load(cls, s: str) -> AdjMatrixGraph:
        g = cls()
        text = io.StringIO(s)
        first_line = next(text)
        v, e = map(int, first_line.strip().split(","))
        assert 0 <= v, "invalid vertex"
        
        g._vsize, g._esize = v, e
        g._adj = [[0 for _ in range(g._vsize)] for _ in range(g._vsize)]
        for line in text:
            line = line.strip()
            if line != "":
                a, b = map(int, line.split(","))
                assert a != b, "self loop edge err"
                assert g._adj[a][b] != 1, "parallel edge"
                g._adj[a][b] = 1
                g._adj[b][a] = 1
        return g
    
    @classmethod
    def dumps(cls, g: AdjMatrixGraph) -> str:
        lines = [f"{g._vsize}, {g._esize}"]
        for ridx in range(g._vsize):
            for cidx in range(ridx, g._vsize):
                if g._adj[ridx][cidx] == 1:
                    lines.append(f"{ridx}, {cidx}")
        return "\n".join(lines)


class TestAdjMatrixGraph(unittest.TestCase):
    
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
        self.g = AdjMatrixGraph.load(s)
    
    def test_dump(self):
        ans = AdjMatrixGraph.dumps(self.g)
        print(ans)
    
    def test_has_edge(self):
        for v in range(self.g.vsize):
            for i in range(self.g.vsize):
                self.assertEqual(self.g.adj[v][i] == 1, self.g.has_edge(v, i))
    
    def test_adj_edge(self):
        self.assertEqual(self.g.adjs(0), [1, 3])
        self.assertEqual(self.g.adjs(1), [0, 2, 6])
        self.assertEqual(self.g.adjs(2), [1, 3, 5])
        self.assertEqual(self.g.adjs(3), [0, 2, 4])
        self.assertEqual(self.g.adjs(4), [3, 5])
        self.assertEqual(self.g.adjs(5), [2, 4, 6])
        self.assertEqual(self.g.adjs(6), [1, 5])


if __name__ == '__main__':
    unittest.main()
