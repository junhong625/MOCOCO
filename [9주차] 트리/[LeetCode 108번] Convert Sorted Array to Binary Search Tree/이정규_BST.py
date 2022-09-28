# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def maketree(stack):
            
            if not stack:
                return
            
            n = len(stack)//2
            
            node = TreeNode(stack[n])
            node.left = maketree(stack[:n])
            node.right = maketree(stack[n + 1:])
            
            return node
        
        
        root = maketree(nums)
        
        return root # 168ms(5.27%) / 16.2mb(44.85%)