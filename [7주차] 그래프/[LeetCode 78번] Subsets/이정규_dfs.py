class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(stack):
            for unit in s_num:
                if not stack or (stack[-1] < unit):
                    stack.append(unit)
                    if stack not in res:
                        res.append(stack[:])
                    dfs(stack)
                    stack.pop()
                
        s_num = sorted(nums)
        res = [[]]
        dfs([])
        
        return res # 282ms / 13.6mb