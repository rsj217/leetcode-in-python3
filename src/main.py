from src.algo.graph.minimum_spanning_tree.prim import prim
from src.algo.graph.shortest_path.dijkstra import dijkstra
from src.datastruct.graph import Graph
from src.datastruct.weight_graph import WeightedGraph
from src.datastruct import graphviz
from src.datastruct.treenode import TreeNode
from src.algo.tree.traversal import *
from src.datastruct.digraph import DiGraph


if __name__ == '__main__':
    """
        0
      /  \
     /     \
    1 ------ 2
     \     / |
      \  /   |
       3 ----4
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
    print(g)
    graphviz.digraph(g)
