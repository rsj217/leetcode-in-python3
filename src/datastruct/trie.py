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
