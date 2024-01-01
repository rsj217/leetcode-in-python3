from src.algo.graph import dfs
from src.datastruct.graph import Graph
from src.datastruct.weight_graph import WeightedGraph
from src.datastruct import graphviz

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
    graphviz.graph(g)
