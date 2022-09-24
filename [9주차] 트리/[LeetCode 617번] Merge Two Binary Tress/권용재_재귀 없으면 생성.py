class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            # 새로운 트리를 생성
            result = TreeNode(root1.val + root2.val)
            result.left = self.mergeTrees(root1.left, root2.left)
            result.right = self.mergeTrees(root1.right, root2.right)
        return result