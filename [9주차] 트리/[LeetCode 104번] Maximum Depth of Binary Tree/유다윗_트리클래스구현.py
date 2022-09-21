# 104. Maximum Depth of Binary Tree

class TreeNode:                                                 # TreeNode 클래스
    def __init__(self, val=None, left=None, right=None):        # LeetCode의 val 파라미터 기본값은 0인데 None으로 바꿈 -> make_tree에서 None을 기준으로 분기하려고
        self.val = val
        self.left = left
        self.right = right


def make_tree(n, root):                                         # 리스트를 인자로 받아서 TreeNode 클래스를 활용해 트리는 만드는 함수
    if n.val != None:                                           # val이 None이 아니라면(즉, 유효한 노드라면)
        if root:                                                # root에 원소가 남아있을 경우,
            left_val = root.pop(0)                              # root의 첫 번째 원소를 pop 해서 왼쪽 자식 인스턴스를 만듦
            n.left = TreeNode(left_val)
            make_tree(n.left, root)                             # 왼쪽 서브트리 만들기

        if root:                                                # root에 원소가 남아있을 경우,
            right_val = root.pop(0)                             # root의 첫 번째 원소를 pop 해서 오른쪽 자식 인스턴스를 만듦
            n.right = TreeNode(right_val)
            make_tree(n.right, root)                            # 오른쪽 서브트리 만들기


def preorder(n, depth):                                         # 전위 순회 함수
    global max_depth
    if n:                                                       # 유효한 노드인 경우,
        preorder(n.left, depth+1)                               # 왼쪽 자식 방문
        preorder(n.right, depth+1)                              # 오른쪽 자식 방문
    else:                                                       # 유효하지 않은 노드인 경우,(즉 노드가 더 이상 없는 경우)
        if depth-1 > max_depth:                                 # 부모 노드의 depth가 max_depth보다 더 클 경우 값 갱신
            max_depth = depth-1
        return


max_depth = 0
def maxDepth(root):
    head = TreeNode(root.pop(0))                                # 트리의 root를 head라는 변수로 지정
    make_tree(head, root)                                       # 트리 만들기
    preorder(head, 0)                                           # 전위 순회
    return max_depth

    
if __name__ == '__main__':
    print(maxDepth([3,9,20,None,None,15,7]))


    
######## leetcode 제출용 ######
# 차이점: 함수의 배치(스코프 고려) / input이 TreeNode 인스턴스로 들어오는데, 이것을 리스트로 변환하는 함수 change_to_list 정의

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# class Solution:
#     def maxDepth(self, root) -> int:
#         temp = []
#         def change_to_list(n):
#             if n:
#                 temp.append(n.val)
#                 change_to_list(n.left)
#                 change_to_list(n.right)
#             else:
#                 temp.append(None)

#         def make_tree(n, root):
#             if n.val != None:
#                 if root:
#                     left_val = root.pop(0)
#                     n.left = TreeNode(left_val)
#                     make_tree(n.left, root)

#                 if root:
#                     right_val = root.pop(0)
#                     n.right = TreeNode(right_val)
#                     make_tree(n.right, root)

#         def preorder(n, depth):
#             nonlocal max_depth
#             if n:
#                 preorder(n.left, depth+1)
#                 preorder(n.right, depth+1)
#             else:
#                 if depth-1 > max_depth:
#                     max_depth = depth-1
#                 return
        
        
#         change_to_list(root)
#         root = temp
#         max_depth = 0
#         head = TreeNode(root.pop(0))
#         make_tree(head, root)
#         preorder(head, 0)
#         return max_depth