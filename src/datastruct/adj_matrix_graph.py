from __future__ import annotations

import unittest
from typing import List
import io
import os


class AdjMatrixGraph:

    def __init__(self):
        self.vsize = 0
        self.esize = 0
        self.adj = None

    def __str__(self):
        title = [str(i) for i in range(self.vsize)]
        title.insert(0, "  ")
        ans = [" ".join(title)]
        for idx, row in enumerate(self.adj):
            newRow = row.copy()
            newRow.insert(0, f"{idx}:")
            ans.append(" ".join(map(str, newRow)))
        return "\n".join(ans)

    def __repr__(self):
        return self.__str__()

    def has_edge(self, v: int, w: int) -> bool:
        assert 0 <= v or 0 <= w, "invalid vertex"
        return self.adj[v][w] == 1

    def adj_edge(self, v: int) -> List[int]:
        assert 0 <= v, "invalid vertex"
        return [i for i in range(self.vsize) if self.adj[v][i] == 1]

    def degree(self, v: int) -> int:
        return len(self.adj_edge(v))

    @classmethod
    def load(cls, s: str) -> AdjMatrixGraph:
        g = cls()
        text = io.StringIO(s)
        first_line = next(text)
        v, e = map(int, first_line.strip().split(","))
        assert 0 <= v, "invalid vertex"

        g.vsize, g.esize = v, e
        g.adj = [[0 for _ in range(g.vsize)] for _ in range(g.vsize)]
        for line in text:
            line = line.strip()
            if line != "":
                a, b = map(int, line.split(","))
                assert a != b, "self loop edge err"
                assert g.adj[a][b] != 1, "parallel edge"
                g.adj[a][b] = 1
                g.adj[b][a] = 1
        return g

    @classmethod
    def dumps(cls, g: AdjMatrixGraph) -> str:
        lines = [f"{g.vsize}, {g.esize}"]
        for ridx in range(g.vsize):
            for cidx in range(ridx, g.vsize):
                if g.adj[ridx][cidx] == 1:
                    lines.append(f"{ridx}, {cidx}")
        return "\n".join(lines)


def graphviz_graph(g: AdjMatrixGraph):
    lines = ["graph g {"]
    for row in range(g.vsize):
        for clo in range(row, g.vsize):
            if g.adj[row][clo] == 1:
                print(f"{row} -- {clo}")
                lines.append(f"{row} -- {clo}")
    lines.append("}")
    with open("graph.dot", "w") as f:
        f.write("\n".join(lines))
    cmd = "dot -T png -o graph.png graph.dot"
    os.system(cmd)
    os.system("open graph.png")


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
        self.assertEqual(self.g.adj_edge(0), [1, 3])
        self.assertEqual(self.g.adj_edge(1), [0, 2, 6])
        self.assertEqual(self.g.adj_edge(2), [1, 3, 5])
        self.assertEqual(self.g.adj_edge(3), [0, 2, 4])
        self.assertEqual(self.g.adj_edge(4), [3, 5])
        self.assertEqual(self.g.adj_edge(5), [2, 4, 6])
        self.assertEqual(self.g.adj_edge(6), [1, 5])


if __name__ == '__main__':
    unittest.main()
