class Solution:
    def longestUnivaluePath(self, root) -> int:
        def dfs(node=root, cnt=0):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
        
            nonlocal maxCnt
            if left + right > maxCnt:
                maxCnt = left + right
            
            return max(left, right)
        maxCnt = 0
        dfs()
   
        return maxCnt