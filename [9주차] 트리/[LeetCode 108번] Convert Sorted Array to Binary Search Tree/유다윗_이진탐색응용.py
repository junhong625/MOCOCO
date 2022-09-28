# 108. Convert Sorted Array to Binary Search Tree
# 62ms / 15.6mb

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def make_height_balanced_tree(arr, n):
            middle = len(arr) // 2                                  # 배열 내 숫자의 중간값 찾기
            
            node = TreeNode(arr[middle])                            # 중간값으로 TreeNode 인스턴스 생성
            if not n.left:                                          # 인자로 받은 부모 노드의 왼쪽 자식이 없을 경우 node를 왼쪽 자식으로 지정
                target = n.left = node
            else:                                                   # 부모 노드의 왼쪽 자식이 있을 경우 node를 오른쪽 자식으로 지정
                target = n.right = node

            if middle-1 != -1:                                      # middle의 왼쪽에 원소가 남아 있을 경우
                make_height_balanced_tree(arr[:middle], target)
            if middle+1 != len(arr):                                # middle의 오른쪽에 원소가 남아 있을 경우
                make_height_balanced_tree(arr[middle+1:], target)
        
        nums.sort()                                                 # 오름차순 정렬
        head=root=TreeNode()                                        # head는 출력을 위한 인스턴스 / root는 함수 인자로 넣기 위한 인스턴스
        make_height_balanced_tree(nums, root)
        return head.left                                            # head.left에 트리가 저장되어 있음