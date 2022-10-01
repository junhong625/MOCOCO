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
        # 구간 안에 있을 경우 왜 더이상의 탐색이 필요가 없을까요?
        #
        self.result = 0
        def tree(x):
            if x:
                if low <= x.val <= high:
                    self.result += x.val
                    tree(x.left)
                    tree(x.right)
                elif x.val < low:
                    tree(x.right)
                else:
                    tree(x.left)
        tree(root)
        return self.result