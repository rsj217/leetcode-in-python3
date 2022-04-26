class Trie:

    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, word: str) -> None:
        prev = self
        for w in word:
            node = prev.children.get(w, None)
            if node is None:
                node = Trie()
                prev.children[w] = node
            prev = node
        node.is_word = True

    def search(self, word: str) -> bool:
        prev = self
        for w in word:
            node = prev.children.get(w, None)
            if node is None:
                return False
            prev = node
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        prev = self
        for w in prefix:
            node = prev.children.get(w, None)
            if node is None:
                return False
            prev = node
        return True


import unittest


class TestTrie(unittest.TestCase):

    def test_create(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))
