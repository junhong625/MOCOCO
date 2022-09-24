# 110. Balanced Binary Tree
# 46ms / 18.8mb

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 후위순회
        # 왼쪽 서브트리 깊이 받기
        # 오른족 서브트리 깊이 받기
        # 만약에 깊이가 1보다 크면 False

        def postorder(n):
            if n:
                left_height = postorder(n.left)
                right_height = postorder(n.right)
                if not self.isBalanced:
                    return
                if abs(left_height - right_height) > 1:
                    self.isBalanced = False
                    return
                else:
                    return max(left_height, right_height) + 1
            else:
                return 0
        
        self.isBalanced = True
        postorder(root)
        return self.isBalanced