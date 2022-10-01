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
        # 중위 순회를 하면서 총 합을 계속해서 쌓아가는 방식. val값을 쌓은 값으로 줘야 한다
        self.stack = 0
        def tree(x):
            if x:
                tree(x.right)
                self.stack += x.val
                x.val = self.stack
                tree(x.left)
                return x.val
            else:
                return 0
        tree(root)
        return root