class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # combinations 함수를 사용한 간단한 풀이
        # from itertools import combinations
        # return list(combinations(range(1, n+1), k))

        # 재귀 dfs를 사용한 풀이
        def dfs(sub): # dfs 함수
            if len(sub) == k:
                result.append(sub)
                return 
            for i in range(sub[-1]+1, n+1):
                dfs(sub+[i])
        
        result = []
        for i in range(1, n+1):
            dfs([i])
        
        return result

        # combinations를 사용한 풀이 약 10~20배 정도의 속도 차이가 남