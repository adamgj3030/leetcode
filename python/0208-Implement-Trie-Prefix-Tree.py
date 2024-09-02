class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()
        
    def insert(self, word: str) -> None:
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = PrefixTreeNode()
            currNode = currNode.children[char]
        currNode.word = True


    def search(self, word: str) -> bool:
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return currNode.word   

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for char in prefix:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return True
