# 문제를 이해 못해서 문자열로 합쳐주고 다시 그걸 트리로 만드는 것인지를 이해 못했습니다
# 내일까지 한번 다시 풀어보겠슴다
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        que = collections.deque([(root)])
        result = ["No"]
        while que:
            node = que.popleft()
            if node:
                que.append(node.left)
                que.append(node.right)
                result.append((str(node.val)))
            else:
                result.append('No')
        return ' '.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'No No':
            return None
        
        nodes = data.split()
        
        print(nodes)
        root = TreeNode(int(nodes[1]))
        que = collections.deque([root])
        index = 2
        while que:
            node = que.popleft()
            if nodes[index] != 'No':
                node.left = TreeNode(int(nodes[index]))
                que.append(node.left)
            index += 1
            
            if nodes[index] != 'No':
                node.right = TreeNode(int(nodes[index]))
                que.append(node.right)
            index += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))