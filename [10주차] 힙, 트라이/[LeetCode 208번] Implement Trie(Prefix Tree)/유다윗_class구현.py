# 208. Implement Trie (Prefix Tree)

# 결국 교재... 쓰읍
from collections import defaultdict

class Tree:
    def __init__(self):
        self.ch = defaultdict(Tree)
        self.check = False

class Trie:
    def __init__(self):
        self.trie = Tree()              # tries 초기화
        
    def insert(self, word: str):
        node = self.trie
        for w in word:
            node = node.ch[w]
        node.check = True

    def search(self, word: str) -> bool:
        node = self.trie
        for w in word:
            if w in node.ch:
                node = node.ch[w]
            else:
                return False
        if node.check:
            return True
        return False

    
    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for w in prefix:
            if w in node.ch:
                node = node.ch[w]
            else:
                return False
        return True















#######################################################

# 14번째 tc에서 막힘
class Tree:
    def __init__(self):
        self.ch = defaultdict(Tree)
        self.check = False

class Trie:
    def __init__(self):
        self.trie = Tree()              # tries 초기화
        
    def insert(self, word: str):
        node = self.trie
        for w in word:
            node = node.ch[w]
        node.check = True

    def search(self, word: str) -> bool:
        node = self.trie
        for w in word[:-1]:
            if len(node.ch[w].keys()):
                node = node.ch[w]
            else:
                return False
        if node.check:
            return True
        return False

    
    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for w in prefix:
            if len(node.ch[w].keys()):
                node = node.ch[w]
            else:
                return False
        return True