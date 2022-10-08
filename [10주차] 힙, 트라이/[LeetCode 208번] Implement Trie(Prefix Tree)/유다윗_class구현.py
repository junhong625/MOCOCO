# 208. Implement Trie (Prefix Tree)
# 14번째 tc에서 막힘

from collections import defaultdict

class Trie:
    tries = defaultdict()                       # key: 루트 키값(word의 첫 글자) / value: 해당 루트의 trie와 final
                                                # final: 각 단어의 끝나는 글자와 그 글자의 인덱스를 넣어둘 리스트
    def __init__(self):
        Trie.tries = defaultdict()              # tries 초기화
        
    def insert(self, word: str):
        if word[0] not in Trie.tries:           # 새로운 알파벳으로 시작하는 단어일 경우 tries에 초기값 할당
            Trie.tries[word[0]] = [defaultdict(set), list()]
        
        trie = Trie.tries[word[0]][0]
        final = Trie.tries[word[0]][1]
        p = -1
        for i in range(len(word)):              # 각 레벨마다 글자 추가
            trie[i].add((word[i], p))
            p = word[i]
        final.append([word[-1], len(word)-1])

    def search(self, word: str) -> bool:
        if word[0] not in Trie.tries:
            return False
        trie, final = Trie.tries[word[0]]
        
        p = -1
        for i in range(len(word)):
            if (word[i], p) not in trie[i]:          # 글자가 없을 경우 False
                return False
            p = word[i]
        if [word[-1], len(word)-1] in final:    # final에 끝나는 글자와 인덱스가 있을 경우 단어가 있으므로 True
            return True
        else:
            return False
    
    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in Trie.tries:
            return False
        trie = Trie.tries[prefix[0]][0]

        p = -1
        for i in range(len(prefix)):
            if (prefix[i], p) not in trie[i]:
                return False
            p = prefix[i]
        else:
            return True                         # fianl은 따로 확인할 필요 없음