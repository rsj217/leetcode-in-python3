
from src.datastruct.treenode import *
from src.datastruct.graphviz import *


nums = [1, 2, 3, None, None, 4,5,7]

# root = TreeNode.deserialize(nums)

root  = deserialize('[1,2,3,null,null,4,5,6,7]')

binary_tree(root)