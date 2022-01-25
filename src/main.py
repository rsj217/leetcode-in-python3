from src.datastruct.b_treenode import *

bt = BTree(order=4)

nums = [3, 1, 5, 4, 2, 9, 10, 8, 7, 6]
nums.reverse()

for i in nums:
    bt.insert(i)

graphviz_tree(bt.root)
