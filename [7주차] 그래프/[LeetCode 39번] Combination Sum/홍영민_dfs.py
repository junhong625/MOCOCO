class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 이전의 조합을 구하는 공식과 동일
        def dfs(x):
            if x and sum(x) == target:
                result.append(x[:])
                return 
            elif x and sum(x) > target:
                return 
            else:
                # 다만, 중복이 되지 않게 하기 위해, 특정 원소 탐색하도록 설정해줘야 한다.
                # 따라서 마지막으로 삽입된 원소의 인덱스 이후로만 반복문이 돌도록 설정
                if x:
                    idx = candidates.index(x[-1])
                else:
                    idx = 0
                # 윗부분은 책의 도식을 보고 작성한 것이다
                # 왜 아직도 반복문이 이렇게 설정되어야 하는지 이해하지 못하고는 있다
                for i in candidates[idx:]:
                    x.append(i)
                    dfs(x)
                    x.pop()
        result = []
        dfs([])
        return result