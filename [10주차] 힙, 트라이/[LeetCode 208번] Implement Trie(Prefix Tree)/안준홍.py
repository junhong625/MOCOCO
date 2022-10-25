class Trie:

    def __init__(self):
        self.trie = {}
        self.st = ''
        
    def insert(self, word: str) -> None:
        std = self.trie
        for i in range(len(word)):
            if word[i] not in std:
                std[word[i]] = Trie()
            std = std[word[i]]
        std.st = word
            
    def search(self, word: str) -> bool:
        std = self.trie
        for char in word:
            if char not in std:
                return False
            std = std[char]
        if std.st == word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        std = self.trie
        for char in prefix:
            if char not in std:
                return False
            std = std[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)