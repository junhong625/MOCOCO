class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(root):
            nonlocal depth
    
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            ## 왼쪽 뎁스 ##
            if root.left and root.val == root.left.val:
                left_depth = left + 1
            else:
                left_depth = 0

            ## 오른쪽 뎁스 ##
            if root.right and root.val == root.right.val:
                right_depth = right + 1
            else:
                right_depth = 0

            ## 최종으로 불러올 뎁스 갱신 ##
            depth = max(depth, left_depth + right_depth)

            ## 함수에서 리턴은 맨 아래 부터에서 누적해온 왼쪽과 오른쪽의 뎁스의 가장 큰 값##
            return max(left_depth, right_depth)
        
        dfs(root)
        return depth