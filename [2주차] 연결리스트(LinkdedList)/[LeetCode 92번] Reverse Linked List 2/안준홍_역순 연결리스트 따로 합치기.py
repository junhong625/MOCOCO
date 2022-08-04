# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # 정렬한 연결리스트가 할당될 변수
        result = dummy = ListNode()
        # 범위 내의 연결리스트를 역순으로 정렬하여 할당할 변수
        rev = reverse = ListNode()
        # 범위에 해당하는 노드인지 확인하기 위한 변수
        count = 1
        # 연결리스트 끝까지 반복
        while head:
            # 순번이 범위 안일 경우
            if count in range(left, right+1):
                # 범위의 시작점일 경우 val만 변경(역순 연결리스트의 끝이 0이 되는걸 방지하기 위해)
                if count == left:
                    rev.val = head.val
                # 범위의 시작점이 아닐 경우 rev를 다음값으로 지정하고 head의 값을 새로운 노드의 val로 넣어 rev에 할당(역순 정렬)
                else:
                    rev = ListNode(head.val, rev)
                # 위 조건을 거친 후 범위의 마지막일 경우 멈춰있는 dummy연결리스트의 다음 포인터를 역순 연결리스트의 시작점으로 지정 후 
                # dummy를 역순 연결리스트의 끝으로 이동 
                if count == right:
                    dummy.next = rev
                    dummy = reverse
            # 순번이 범위 밖일 경우 dummy연결리스트의 다음포인터로 현재 head를 지정 후 다음포인터로 이동
            else:
                dummy.next = head
                dummy = dummy.next
            # 연결리스트를 다음 포인터로 이동
            head = head.next
            count += 1
        # 시작점의 val은 0이고 정답은 다음포인터부터 시작이기에 다음 포인터를 반환
        return result.next