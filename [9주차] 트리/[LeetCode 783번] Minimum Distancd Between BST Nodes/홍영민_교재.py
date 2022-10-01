# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 왼쪽에선 가장 큰 숫자를, 오른쪽에선 가장 작은 숫자를
        result = 10**5
        prev = -10**5
        stack = []
        node = root
        while stack or node:
            while node: # 왼쪽을 모두 탐색 후에 스택에 저장
                stack.append(node)
                node = node.left
            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val # 이후 중간 노드가 계산에 활용될 수 있도록 설정
            # 오른쪽으로 하나 탐색을 진행, 만약 있으면 위의 while문에서 오른쪽 탐색이 진행 될 것임
            node = node.right
        return result
    # 그냥 모든 노드값 리스트에 저장해서 크기 비교,
    # 장점은 모든 노드를 비교할 필요 없어서 시간이 엄청나게 단축됨
    # 다만, 새 리스트를 만드는 것이므로 만약 데이터가 크다면 메모리 측면에서 손해를 볼것임
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 왼쪽에선 가장 큰 숫자를, 오른쪽에선 가장 작은 숫자를

        stack = []

        def tree(x):
            if x:
                stack.append(x.val)
                tree(x.left)
                tree(x.right)

        tree(root)
        stack.sort()
        result = 10 ** 5
        for i in range(len(stack) - 1):
            k = stack[i + 1] - stack[i]
            if k < result:
                result = k
        return result