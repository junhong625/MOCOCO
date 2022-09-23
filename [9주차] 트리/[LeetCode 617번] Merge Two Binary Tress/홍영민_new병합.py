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
        # 아무것도 없을 때의 예외 처리
        if not root1 and not root2:
            return root1
        new = TreeNode()
        
        # 트리를 더 진행해야 하는 경우는 둘 중 하나의 값이라도 있어야 하는 조건
        # 따라서 진행 전에 미리 if문을 통해 검사
        # 안하면 미리 treenode를 만들어 버려서 이상하게 됨
        def adding(x,y,new):
            if x or y:
                if not x:
                    x = TreeNode()
                if not y:
                    y = TreeNode()
                new.val = x.val + y.val
                if x.right or  y.right:
                    new.right = TreeNode()
                    adding(x.right, y.right, new.right)
                if x.left or y.left:
                    new.left = TreeNode()
                    adding(x.left, y.left, new.left)

        adding(root1, root2, new)
        return new