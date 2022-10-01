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
        if not inorder:
            return
        
        root = preorder.pop(0)
        for n in range(len(inorder)):
            if inorder[n] == root:
                break
        
        node = TreeNode(inorder[n])
        node.left = self.buildTree(preorder, inorder[:n])
        node.right = self.buildTree(preorder, inorder[n + 1:])
            
        return node
    
'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        root = TreeNode(preorder[0])
        
        for idx in range(len(inorder)):
            if inorder[idx] == preorder[0]:
                break
        
        def make(hubo):
            if not hubo:
                return
            
            n = len(hubo) // 2
            
            node = TreeNode(hubo[n])
            node.left = make(hubo[:n])
            node.right = make(hubo[n + 1:])
            
            return node
        
        root.left = make(inorder[:idx])
        root.right = make(inorder[idx + 1:])
            
            
        print(root)
        return root
'''
