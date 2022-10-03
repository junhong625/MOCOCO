class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        def preorder(root=root):                # 전위 순회 탐색
            if low <= root.val <= high:         # 값이 범위 안일 경우 total에 더해주기
                self.total += root.val          
            if root.val > low and root.left:    # 값이 low보다 클 경우 왼쪽 자식 노드 탐색
                preorder(root.left)
            if root.val < high and root.right:  # 값이 high보다 작을 경우 오른쪽 자식 노드 탐색
                preorder(root.right)
        preorder()                              # 전위 순회 시작!
        return self.total