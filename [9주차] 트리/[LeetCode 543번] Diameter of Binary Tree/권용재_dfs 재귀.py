def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def level(root):
            nonlocal diameter
            if not root:
                return 0
            left = level(root.left)
            right = level(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        level(root)

        return diameter