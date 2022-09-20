class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(p, p_idx, root):
    left_idx = p_idx*2
    if left_idx > len(root)-1:
        return
    p.left = TreeNode(root[left_idx])
    make_tree(p.left, left_idx, root)

    right_idx = p_idx*2+1
    if right_idx > len(root)-1:
        return
    p.right = TreeNode(root[right_idx])
    make_tree(p.right, right_idx, root)


def preorder(n, depth):
    global max_depth
    if n:
        print(n.val)
        preorder(n.left, depth+1)
        preorder(n.right, depth+1)
    else:
        
        if depth > max_depth:
            max_depth = depth
        return
        

max_depth = 0
def maxDepth(root):
    if root == []:
        return 0
    # root를 인덱스 1로 두기 위해 root 앞에 0 추가
    root.insert(0, 0)

    # root를 순회하며 각 숫자를 val로 TreeNode 인스턴스 만든 후, 왼쪽 노드는 x2한 인덱스의 값으로, 오른쪽 노드는 x2+1한 인덱스 값으로 지정
    head = TreeNode(root[1])
    make_tree(head, 1, root)

    preorder(head, 0)

    return max_depth

if __name__ == '__main__':
    print(maxDepth([1,2,None,3,None,4,None,5]))
    print()