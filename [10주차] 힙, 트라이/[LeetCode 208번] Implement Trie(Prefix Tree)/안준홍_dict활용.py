class Trie:

    def __init__(self, data=None):
        self.trie = {}
        self.data = data
        
    def insert(self, word: str) -> None:
        std = self
        for char in word:
            if char not in std.trie:
                std.trie[char] = Trie()
            std = std.trie[char]
        std.data = word
            
    def search(self, word: str) -> bool:
        std = self
        for char in word:
            if char not in std.trie:
                return False
            std = std.trie[char]
        return True if std.data == word else False
        
    def startsWith(self, prefix: str) -> bool:
        std = self
        for char in prefix:
            if char not in std.trie:
                return False
            std = std.trie[char]
        return True