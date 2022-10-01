# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 오른쪽 왼쪽 잘라서 재귀로 돌림
        # 다만, 잘라서 따로 저장하니까 메모리 손해가 큼
        leaf = preorder.pop(0)
        slicing = inorder.index(leaf)
        left_in = inorder[:slicing]
        right_in = inorder[slicing+1:]
        left_pre = preorder[:slicing]
        right_pre = preorder[slicing:]
        root = TreeNode(leaf)
        if left_in:
            root.left = self.buildTree(left_pre, left_in)
        if right_in:
            root.right = self.buildTree(right_pre, right_in)
        return root