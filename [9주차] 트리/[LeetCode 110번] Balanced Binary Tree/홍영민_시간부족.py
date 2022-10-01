# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 밸런스 상황은 모든 리프 노드들에 대해서 깊이 차이가 2가 나서는 안된다
class Solution(object):
    def isBalanced1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        leaf1 = []
        def leaf(x,s):
            if x:
                if not x.right and not x.left:
                    leaf1.append(s)
                else:
                    leaf(x.right, s+1)
                    leaf(x.left, s+1)

        leaf(root, 1)
        print(leaf1)
        if abs(min(leaf1) - max(leaf1))<=1:
            return True
        else:
            return False
# 새로 작성
    
    def isBalanced(self, root):

        if not root:
            return True
        leaf1 = []
        def leaf(x):
            if x:
                right = leaf(x.right)
                left = leaf(x.left)
                leaf1.append(abs(right-left))
                return max(right, left) + 1
            else:
                return 0
        leaf(root)
        print(leaf1)
        for i in leaf1:
            if i > 1:
                return False
        else:
            return True
