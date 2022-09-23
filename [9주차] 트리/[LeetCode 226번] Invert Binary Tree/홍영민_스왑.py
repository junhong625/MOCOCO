class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def change(x):
            if x:
                x.right, x.left = change(x.left), change(x.right)
                return x
        change(root)
        return root
    # 왜 아래게 위에거보다 절반의 시간이 걸릴까요?
    # 아마 예상은, 우선 전환 이전에 재귀를 통해 말단트리로 진행하고 그 아래서부터 차분히 바꿔가기 때문에 위에 작업
    # 보다는 확실히 움직이는 데이터의 양이 적어질 거 같습니다.
    def invertTree1(self, root):
        if root:
            root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None