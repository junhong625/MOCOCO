# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lens = []
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            
            lens.append(left + right + 2)
            return max(left, right) + 1
        
        dfs(root)
        return max(lens) # 26ms(97.03%) / 16.4mb(19.76%)