# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        dummy = result = ListNode()                                     # 정답이 될 result와 복사본 dummy 생성
        while head:                                                     # head가 존재할 경우 반복
            while dummy.next and head.val > dummy.val:                  # 복사본의 다음값이 존재하고 head의 값보다 복사본의 값이 작을 경우
                dummy = dummy.next                                      # 복사본 다음 노드로 이동
            node, dummy.val = ListNode(dummy.val), head.val             # 현재 복사본 노드의 값을 가진 노드를 생성하고 현재 복사본 노드의 값에 head의 값을 집어넣기
            dummy.next, node.next, head = node, dummy.next, head.next   # 복사본의 다음 노드로 새로 생성한 노드를 지정, 생성한 노드의 다음을 복사본의 다음 노드로 지정, head를 다음 노드로 이동
            
            if head and dummy.val > head.val:                           # 반복문이 끝난 후 head가 존재하고 복사본의 값이 head의 값보다 클 경우
                dummy = result                                          # 복사본을 result의 제일 처음 노드로 변경
        
        while dummy and dummy.next:                                     # 마지막에 노드에 남은 0을 제거하는 반복문
            if not dummy.next.next and dummy.next.val == 0:
                dummy.next = None
                break
            dummy = dummy.next
        return result