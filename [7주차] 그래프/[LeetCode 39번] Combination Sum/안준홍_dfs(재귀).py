class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(sub, i): # dfs 재귀
            if sum(sub) >= target: # target 이상일 경우에 중지
                if sum(sub) == target: # target과 같을 경우에 result에 추가
                    result.append(sub)
                return
            
            for n in range(i, len(candidates)): # 중지 되지 않았다면 다음 깊이 탐색 시작
                dfs(sub + [candidates[n]], n)
        
        result = []
        for i in range(len(candidates)):
            dfs([candidates[i]], i)
        
        return result