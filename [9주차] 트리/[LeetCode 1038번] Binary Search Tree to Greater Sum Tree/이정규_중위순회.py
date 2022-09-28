# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        nujuk = [0]                 # 탐색이 항상 왼쪽부터 가란 법은 없으니깐?
        def jung(node):
            if not node:
                return
            
            jung(node.right)
            nujuk[0] += node.val    # 제일 큰 놈 것부터 더해가면서 백트래킹
            node.val = nujuk[0]
            jung(node.left)
            
            return node
        
        return jung(root) #37ms(22.5%) / 13.7mb(9.17%)