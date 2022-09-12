class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(sub, i): # dfs 재귀 함수
            result.append(sub)
            if len(sub) == len(nums):
                return
            for idx in range(i+1, len(nums)):
                dfs(sub+[nums[idx]], idx)
                
        result = [[]]
        for i in range(len(nums)):
            dfs([nums[i]], i)
        
        return result