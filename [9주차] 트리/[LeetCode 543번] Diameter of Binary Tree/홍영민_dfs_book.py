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
        self.long = 0 
        def tree(x):
            if x:
                left = tree(x.left)
                right = tree(x.right)
                self.long = max(self.long, left + right)
                # print(self.long)
                return max(left, right) + 1 # +1을 해주는 것은, 깊이당 1을 더해주는 과정
            else:
                return 0
        tree(root)
        return self.long