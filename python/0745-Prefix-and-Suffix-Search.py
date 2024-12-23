class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for index, word in enumerate(words):
            length = len(word)
            for i in range(length + 1):
                suffix = word[i:]
                key = f"{suffix}#{word}"
                self._add_to_trie(key, index)


    def _add_to_trie(self, word: str, index: int):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.index = index        

    def f(self, pref: str, suff: str) -> int:
        key = f"{suff}#{pref}"
        cur = self.root
        for c in key:
            if c not in cur.children:
                return -1
            cur = cur.children[c]
        return cur.index

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
