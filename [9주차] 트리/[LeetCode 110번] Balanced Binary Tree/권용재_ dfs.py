class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def level(root):
            if not root:
                return 0
            left = level(root.left)
            right = level(root.right)

            if left <0 or right <0 or abs(left-right) > 1:
                return -1

            return max(left, right) + 1

        def balance(root):
            if level(root) == -1:
                return False
            else:
                return True
                
        return balance(root)