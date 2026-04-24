class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        dummy = self.root
        for char in word:
            if char not in dummy.children:
                dummy.children[char] = TrieNode()
            dummy = dummy.children[char]
        dummy.isWord = True

    def search(self, word: str) -> bool:
        dummy = self.root
        for char in word:
            if char not in dummy.children:
                return False
            dummy = dummy.children[char]
        return dummy.isWord

    def startsWith(self, prefix: str) -> bool:
        dummy = self.root
        for char in prefix:
            if char not in dummy.children:
                return False
            dummy = dummy.children[char]
        return True