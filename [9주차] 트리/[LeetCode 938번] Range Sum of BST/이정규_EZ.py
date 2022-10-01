# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        res = [0]
        def jung(node):
            
            if not node:
                return
            
            jung(node.right)
            if low <= node.val <= high:
                res[0] += node.val
            jung(node.left)
        
        jung(root)
        
        return res[0]