class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        def inorder(root):          # 일반적인 중위 순회가 아닌 오른쪽-부모-왼쪽 순서로 진행하는 중위 순회
            if root.right:
                inorder(root.right)
            nonlocal total
            total += root.val
            root.val = total
            if root.left:
                inorder(root.left)
        inorder(root)
        return root