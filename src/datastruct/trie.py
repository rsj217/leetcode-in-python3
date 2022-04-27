import os


class Trie:

    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, word: str) -> None:
        node = self
        for w in word:
            if node.children.get(w, None) is None:
                node.children[w] = Trie()
            node = node.children[w]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self
        for w in word:
            if node.children.get(w, None) is None:
                return False
            node = node.children[w]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self
        for w in prefix:
            if node.children.get(w, None) is None:
                return False
            node = node.children[w]
        return True


def graphviz_trie(node: Trie):
    def dfs(node, cur_label):
        nonlocal seq
        if len(node.children) <= 0:
            return
        for k, v in node.children.items():
            seq += 1
            next_label = f'node{seq}'
            lines.append(f'\t{next_label}[label="{k}"];\n')
            lines.append(f'\t{cur_label}->{next_label};\n')
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
    cmd = "dot -Tpng -o trie.png trie.dot"
    os.system(cmd)
    os.system("open trie.png")


import unittest


class TestTrie(unittest.TestCase):

    def test_insert_search(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

        graphviz_trie(trie)

    def test_more(self):
        trie = Trie()
        trie.insert("apple")
        trie.insert("hello")
        trie.insert("wow")
        trie.insert("what")
        trie.insert("where")

        graphviz_trie(trie)
