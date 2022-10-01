# 938. Range Sum of BST
# 226ms / 23.1mb

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## 문제 풀며 새삼 깨달은 한 가지: 연관된 조건이면 if if if보다 if elif else로 쓰는 게 효율적이다.
## 왜냐하면 앞쪽 조건이 충족되면 뒷쪽 조건문은 확인할 필요가 없기 때문이다.

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def preorder(n):
            nonlocal result
            if n:
                if n.val > high:        # 현재 노드 값이 high보다 크면 오른쪽 서브트리는 갈 필요가 없음
                    preorder(n.left)
                elif n.val < low:       # 현재 노드 값이 low보다 작으면 왼쪽 서브트리는 갈 필요가 없음
                    preorder(n.right)
                else:
                    preorder(n.left)
                    preorder(n.right)
                    result += n.val
                    
        result = 0
        preorder(root)
        return result