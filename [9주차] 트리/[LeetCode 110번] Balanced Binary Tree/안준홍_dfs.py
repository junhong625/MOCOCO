class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        def dfs(node=root):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            nonlocal result
            if result < abs(left - right):
                result = abs(left - right)
                
            return left+1 if left > right else right+1
        result = 0
        dfs()
        return True if result <= 1 else False