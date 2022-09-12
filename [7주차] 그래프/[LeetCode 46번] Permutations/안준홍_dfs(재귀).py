class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(sub): # dfs 재귀 구현
            if len(sub) == len(nums):
                result.append(sub)
                return
            for i in range(len(nums)):
                if nums[i] not in sub:
                    dfs(sub + [nums[i]])         
        
        result = []
        
        for i in range(len(nums)):
            dfs([nums[i]])
        return result