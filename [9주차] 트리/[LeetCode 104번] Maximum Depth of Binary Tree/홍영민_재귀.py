# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def tree(x,n):
            if x and x.val != None:
                tree(x.left, n+1)
                tree(x.right, n+1)
            else:
                if n-1 > self.result: # 왼쪽만 있을 경우 오른쪽이 마지막에 돌아서 1개가 적게 나온다
                    self.result = n-1 # 위의 상황을 방지하기 위해 크기비교를 통해 큰거를 유지
        tree(root,1)
        return self.result