# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        list_node = []
        
        def tamseack(node):
            if not node:
                return
            
            list_node.append(node.val)
            tamseack(node.left)
            tamseack(node.right)
        
        tamseack(root)
        list_node.sort()
        for i in range(len(list_node) - 1):
            list_node[i] = list_node[i + 1] - list_node[i]
            
        return min(list_node)