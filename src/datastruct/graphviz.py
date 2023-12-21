import os
import collections
from treenode import TreeNode, deserialize
from bs_treenode import BSTreeNode
from b_treenode import BTreeNode
from n_treenode import NTreeNode
from adj_matrix_graph import AdjMatrixGraph
from adj_list_graph import AdjListGraph
from trie import Trie


def leetcode_tree(s: str):
    node = deserialize(s)
    binary_tree(node)


def binary_tree(node: TreeNode | BSTreeNode):
    if node is None:
        return

    seq = 1
    queue = [(node, seq)]

    lines = []
    lines.append('digraph g {\n')
    lines.append('node [shape=record, height=.1];\n')
    lines.append(f'node{seq}[label="<f0> |{node.val}| <f1>"];\n')
    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            node, seq = queue.pop(0)
            if node.left is not None:
                queue.append((node.left, 2 * seq))
                lines.append(f'node{2 * seq}[label="<f0> |{node.left.val}| <f1>"];\n')
                lines.append(f'node{seq}:f0 -> node{2 * seq};\n')

            if node.right is not None:
                queue.append((node.right, 2 * seq + 1))
                lines.append(f'node{2 * seq + 1}[label="<f0> |{node.right.val}| <f1>"];\n')
                lines.append(f'node{seq}:f1 -> node{2 * seq + 1};\n')
    lines.append('}')
    with open("tree.dot", "w") as f:
        f.writelines(lines)
    cmd = "dot -T png -o tree.png tree.dot"
    os.system(cmd)
    os.system("open tree.png")


def ntree(node: NTreeNode):
    if node is None:
        return None

    seq = 0
    lines = []
    lines.append('digraph g {')
    lines.append('node [shape=record, height=.1];\n')
    lines.append(f'node{seq}[label="{node.val}"];\n')

    queue = [(node, f'node{seq}')]

    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            node, parent = queue.pop(0)
            for i in node.children:
                seq += 1
                queue.append((i, f'node{seq}'))
                lines.append(f'node{seq}[label="{i.val}"];\n')
                lines.append(f'{parent} -> node{seq};\n')

    lines.append('}')
    with open("ntree.dot", "w") as f:
        f.writelines(lines)
    cmd = "dot -T png -o ntree.png ntree.dot"
    os.system(cmd)
    os.system("open ntree.png")


def btree(node: BTreeNode):
    def draw_label(node_: BTreeNode) -> str:
        i = 0
        label_ = f"<f{i}>"
        while i < len(node_.keys):
            label_ += f" |{node_.keys[i]}| <f{i + 1}>"
            i += 1
        return label_

    root = node
    label = draw_label(root)
    seq = 0
    lines = []
    lines.append('digraph g {\n')
    lines.append('node [shape=record, height=.1];\n')
    lines.append(f'node{seq}[label="{label}"];\n')

    queue = collections.deque()
    queue.append((root, f"node{seq}"))
    while len(queue) > 0:
        size = len(queue)
        for _ in range(size):
            node, parent = queue.popleft()
            for i, v in enumerate(node.children):
                if v is not None:
                    seq += 1
                    label = draw_label(v)
                    lines.append(f'node{seq}[label="{label}"];\n')
                    lines.append(f'"{parent}": f{i} -> "node{seq}"\n')
                    queue.append((v, f'node{seq}'))
    lines.append("}")
    with open("btree.dot", "w") as f:
        f.writelines(lines)
    cmd = "dot -T png -o btree.png btree.dot"
    os.system(cmd)
    os.system("open btree.png")


def adjmatrix_graph(g: AdjMatrixGraph):
    lines = ["graph g {"]
    for row in range(g.vsize):
        for clo in range(row, g.vsize):
            if g.adj[row][clo] == 1:
                lines.append(f"{row} -- {clo}")
    lines.append("}")
    with open("adjmatrix_graph.dot", "w") as f:
        f.write("\n".join(lines))
    cmd = "dot -T png -o graph.png graph.dot"
    os.system(cmd)
    os.system("open graph.png")


def adjlist_graph(g: AdjListGraph):
    lines = ["graph g {"]
    for k, v in g._adj.items():
        lines.extend([f"{k} -- {i}" for i in v if k < i])
    lines.append("}")
    with open("graph.dot", "w") as f:
        f.write("\n".join(lines))
    cmd = "dot -T png -o graph.png graph.dot"
    os.system(cmd)
    os.system("open graph.png")


def trie(node: Trie):
    def dfs(node, curr_label):
        nonlocal seq
        if len(node.children) <= 0:
            return
        for k, v in node.children.items():
            seq += 1
            next_label = f'node{seq}'
            lines.append(f'\t{next_label}[label="{k}"];\n')
            lines.append(f'\t{curr_label}->{next_label};\n')
            dfs(v, next_label)

    seq = 0
    lines = []
    lines.append('digraph g {\n')
    lines.append('\tnode [height=.1];\n')
    lines.append('\tnode0[label=root];\n')
    dfs(node, "node0")
    lines.append('}')

    with open("trie.dot", "w") as f:
        f.writelines(lines)
    cmd = "dot -T png -o trie.png trie.dot"
    os.system(cmd)
    os.system("open trie.png")
