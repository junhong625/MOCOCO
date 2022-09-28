# 1038. Binary Search Tree to Greater Sum Tree
# 36ms / 13.8mb

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def greater_sum_tree(n, from_p):                        # 오른쪽 자식 노드부터 방문하는 중위순회
            if n:
                right = greater_sum_tree(n.right, from_p)       # 오른쪽 자식 노드로부터 값을 받음
                n.val += right + from_p                         # 현재 노드의 val에 부모로부터 받은 값과 오른쪽 자식 노드로부터 받은 값을 더해줌
                left = greater_sum_tree(n.left, n.val)          # 왼쪽 자식 노드로부터 값을 받음
                return n.val - from_p + left                    
            else:
                return 0
        
        greater_sum_tree(root, 0)
        return root