# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        gipis = []
        def gipi(node):
            if not node:                            # 없는 노드면 0리턴
                return 0
        
            gaps = []                               # 각 노드 깊이 모으기
            gaps.append(gipi(node.left))
            gaps.append(gipi(node.right))
            
            if 'out' in gaps or abs(gaps[0] - gaps[1]) > 1:
                return 'out'                        # 'out'이 있거나 값 차이 1보다 크면 'out 리턴
            else:
                return max(gaps) + 1                # 아니면 자식 노드 중 가장 깊은 것에 자기 포함해서 리턴
        
        
        return gipi(root) != 'out' # 62ms(56.75%) / 19.3mb(7.58%)