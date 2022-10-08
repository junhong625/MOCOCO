class TrieNode():
    def __init__(self):
        self.children = dict()
        self.end = False
        self.idx = -1


root = TrieNode()
n, m = map(int, input().split())
for _ in range(n):
    cur = root
    word = input()
    for j in range(len(word)):
        if word[j] not in cur.children:
            cur.children[word[j]] = TrieNode()
        cur = cur.children[word[j]]
result = 0
for _ in range(m):
    cur = root
    not_in = True
    word = input()
    for j in range(len(word)):
        if word[j] not in cur.children:
            not_in = False
            break
        cur = cur.children[word[j]]
    if not_in == True:
        result += 1
print(result)
        