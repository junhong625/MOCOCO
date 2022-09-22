# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lens = []
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:     # 존재하고 같으면 추가
                left += 1
            else:                                           # 아니라면 초기화
                left = 0
            
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            lens.append(left + right)                       # 둘 다 값이 있으면 합치는 게 맞고
                                                            # 둘 중 하나만 선택됐으면 한 쪽 값만 들어가고
            return max(left, right)
        
        dfs(root)
        
        if lens:
            return max(lens) # 322ms(97.24%) / 20.7mb(17.24%)
        else:
            return 0