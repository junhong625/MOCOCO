# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        
        def dfs(node1, node2):                              # node1로 병합
            if node1 and node2:
                node1.val += node2.val
                node1.left = dfs(node1.left, node2.left)
                node1.right = dfs(node1.right, node2.right)
                return node1
            
            elif not node1 and node2:
                return node2
            else:
                return node1
        
        return dfs(root1, root2) # 173ms(7.83%) / 14,8mb(21.11%)