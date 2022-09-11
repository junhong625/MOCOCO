class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def dfs(x,t):
            # 마지막 원소 이상으로 나아가면 중단
            if t > len(nums):
                return
            else:
                result.append(x[:])
                # 마지막으로 붙여버린 원소의 위치 이후에서 탐색 진행
                for i in nums[t:]:
                    dfs(x+[i],nums.index(i)+1)
        dfs([],0)
        return result