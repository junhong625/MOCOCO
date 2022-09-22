# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        
        def bfs(node):
            stack = collections.deque([node])
            
            while stack:
                s = stack.popleft()
                if s:
                    ans.append(str(s.val))
                else:
                    ans.append('null')                
                if s:
                    stack.append(s.left)
                    stack.append(s.right)
                
        bfs(root)
        
        while ans and ans[-1] == 'null':
            ans.pop()
        
        return ' '.join(ans)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return []
        
        LtoN = []
        for unit in data.split():
            if unit.isdigit():
                LtoN.append(int(unit))
            else:
                LtoN.append(unit)
        
        res = TreeNode(LtoN[0])
        
        stack = collections.deque([res])
        for i in range(len(LtoN)//2):
            node = stack.popleft()
            if len(LtoN) > 2 * i + 1:
                if LtoN[2 * i + 1] != 'null':
                    node.left = TreeNode(LtoN[2 * i + 1])
                    stack.append(node.left)
            if len(LtoN) > 2 * i + 2:
                if LtoN[2 * i + 2] != 'null':
                    node.right = TreeNode(LtoN[2 * i + 2])
                    stack.append(node.right)
        
        return res # 372ms(24.71%) / 23.4mb(73.93%)
            
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))