class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_jewels = {}                        # 해시 테이블

        for j in jewels:
            hash_jewels.update({j : 1})         # 보석을 key로, 1을 value로 추가

        result = 0                              # 결과값
        for s in stones:
            try:
                result += hash_jewels[s]        # stones를 순회하며 보석일 경우 +1
            except:
                pass

        return result