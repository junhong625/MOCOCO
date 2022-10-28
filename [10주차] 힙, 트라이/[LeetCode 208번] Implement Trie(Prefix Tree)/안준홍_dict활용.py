class Trie:

    def __init__(self):
        self.trie = {}                              # dictionary로 trie 구현
        self.end = False                            # 단어의 끝 지점을 표시하는 기준이 될 변수 
        
    def insert(self, word: str) -> None:
        std = self                                  # std를 기준으로 설정
        for char in word:                           # 단어에서 문자를 하나씩 순회
            if char not in std.trie:                # 해당 문자가 trie에 없을 경우
                std.trie[char] = Trie()             # trie에 Key를 문자로, value를 Trie 클래스로 설정한 dict 생성
            std = std.trie[char]                    # 해당 문자로 std(기준점) 이동
        std.end = True                              # 순회가 끝난 후 마지막 기준점에 단어의 끝 지점이라는 의미로 True로 변경 
            
    def search(self, word: str) -> bool:
        std = self                                  # std를 기준으로 설정
        for char in word:                           # 단어에서 문자를 하나씩 순회
            if char not in std.trie:                # 해당 문자가 trie에 없을 경우
                return False                        # False를 반환
            std = std.trie[char]                    # 해당 문자로 std(기준점) 이동
        return std.end                              # 순회가 끝난 후 마지막 기준점에 존재하는 end로 해당 단어가 존재하는지 아닌지 판단
        
    def startsWith(self, prefix: str) -> bool:
        std = self                                  # std를 기준으로 설정
        for char in prefix:                         # prefix에서 문자를 하나씩 순회
            if char not in std.trie:                # 문자가 trie에 없을 경우 
                return False                        # 접두사에 해당되지 않기에 False를 반환
            std = std.trie[char]                    # 해당 문자로 std(기준점) 이동
        return True                                 # 순회를 무사히 마쳤다면 접두사이기에 True를 반환