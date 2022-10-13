# 147. Insertion Sort List
# 1026ms / 17.3mb

# flow
# 1. 정렬된 리스트를 넣을 리스트 만들기
# 2. head에서 하나씩 빼서 정렬된 리스트에 넣기

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = []
        while head:
            for i in range(len(sorted_list)-1, -1, -1):     # 정렬 리스트를 역순으로 순회하며 head.val
                if head.val >= sorted_list[i]:
                    sorted_list.insert(i+1, head.val)
                    break
            else:                                           # for문이 중단되지 않았으면 첫 번째 원소로 추가
                sorted_list.insert(0, head.val)
            head = head.next
        root = node = ListNode()
        for i in sorted_list:                               # ListNode 만들기
            node.next = ListNode(i)
            node = node.next
        return root.next
                 