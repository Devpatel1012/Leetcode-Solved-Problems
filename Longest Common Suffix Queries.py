class TrieNode:
    def __init__(self):
        self.children = {}
        self.min_len = float("inf")
        self.idx = float("inf")


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, idx):
        node = self.root

        # Update root info
        if len(s) < node.min_len:
            node.min_len = len(s)
            node.idx = idx

        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()   # FIXED

            node = node.children[ch]

            if len(s) < node.min_len:
                node.min_len = len(s)
                node.idx = idx

    def query(self, s):
        node = self.root

        for ch in s:
            if ch in node.children:
                node = node.children[ch]
            else:
                break

        return node.idx


class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        trie = Trie()

        # FIXED variable name
        for i, word in enumerate(wordsContainer):
            reverseword = word[::-1]
            trie.insert(reverseword, i)

        res = []

        # FIXED variable name
        for query in wordsQuery:
            reversequery = query[::-1]

            # FIXED method call syntax
            res.append(trie.query(reversequery))

        return res