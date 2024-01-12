
from src.algo.tree.traversal import *
from src.datastruct.treenode import TreeNode
from src.datastruct.graphviz import *



s = [4, 3, 5, 1, 2]


root = TreeNode.deserialize(s)



ans1 = list(inorder_dfs(root))
print(ans1)


ans2 = list(inorder_traversal(root))
print(ans2)


ans3 = list(levelorder_travel(root))
print(ans3)


