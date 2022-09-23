# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.long = 0

        def tree(x):
            if x:
                # 현 시점을 루트로 하여 탐색 시작
                right = tree(x.right)
                left = tree(x.left)
                # 만약 동일하면 길이를 부여 / 아니면 0으로 환산
                if x.right and x.right.val == x.val:
                    right += 1
                else:
                    right = 0

                if x.left and x.left.val == x.val:
                    left += 1
                else:
                    left = 0
                self.long = max(self.long, right + left)
                return max(right, left)
            else:
                return 0

        tree(root)
        return self.long