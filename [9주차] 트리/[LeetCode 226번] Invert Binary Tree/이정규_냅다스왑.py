# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inv(node):
            if not node:
                return
            
            node.left, node.right = inv(node.right), inv(node.left) # 파이썬 갓갓 스왑
            
            return node
        
        inv(root)
        
        return root # 34ms(26.74%) / 13.5mb(49.61%)