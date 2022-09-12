class Solution:
    def combine(self, n, k):
 
        def dfs(stack, s, k):
            if k == 0:
                res.append(stack[:])
                return
 
            for i in range(s, n + 1):
                stack.append(i)
                dfs(stack, i + 1, k - 1)
                stack.pop()
 
        res = []
        dfs([], 1, k)
        return res # 1446ms / 15mb