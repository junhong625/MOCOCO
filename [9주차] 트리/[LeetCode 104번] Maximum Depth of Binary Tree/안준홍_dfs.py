class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## dfs 탐색으로 최대 깊이 탐색
        def dfs(node=root, cnt=1): 
            nonlocal result # result가 현재 global 위치가 아니기에 nonlocal로 호출
            if node.left:
                dfs(node.left, cnt+1)
            if node.right:
                dfs(node.right, cnt+1)
            result = result if result > cnt else cnt
        
        result = 0

        if root:
            dfs()
        return result