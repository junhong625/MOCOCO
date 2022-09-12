class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def dfs(stack, t):
            if t == 0:
                if stack not in res:
                    res.append(stack[:])
                return
            elif t < 0:
                return
 
            for unit in s_can:
                if not stack or (stack[-1] <= unit):
                    stack.append(unit)
                    dfs(stack, t - unit)
                    stack.pop()
                
        s_can = sorted(candidates)
        res = []
        dfs([], target)
        
        return res # 282ms / 13.6mb