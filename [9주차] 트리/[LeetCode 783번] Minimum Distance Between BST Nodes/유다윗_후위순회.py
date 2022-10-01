# 783. Minimum Distance Between BST Nodes
# 51ms / 14mb

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 이진탐색트리기 때문에 가능한 풀이법 -> 왼쪽 서브트리의 가장 큰 값, 오른쪽 서브트리의 가장 작은 값과 비교하면 됨

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def postorder(n):
            nonlocal min_dist
            if n:
                try:
                    left = list(postorder(n.left))
                except:
                    left = None
                try:
                    right = list(postorder(n.right))
                except:
                    right = None

                if not left and not right:              # left right 둘 다 없을 경우
                    return n.val, n.val
                elif left and right:                    # left right 둘 다 있을 경우
                    if min_dist > n.val - left[1]:
                        min_dist = n.val - left[1]
                    if min_dist > right[0] - n.val:
                        min_dist = right[0] - n.val
                    return left[0], right[1]
                elif left:                              # left만 있을 경우
                    if min_dist > n.val - left[1]:
                        min_dist = n.val - left[1]
                    return left[0], n.val
                else:                                   # right만 있을 경우
                    if min_dist > right[0] - n.val:
                        min_dist = right[0] - n.val
                    return n.val, right[1]
        
        
        min_dist = 1e5
        postorder(root)
        return min_dist