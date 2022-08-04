# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 홀수 연결리스트(val을 넣지 않았기에 0부터 시작)
        result = odd = ListNode()
        # 짝수 연결리스트(val을 넣지 않았기에 0부터 시작)
        dummy = even = ListNode()
        # 순번을 계산해줄 변수
        count = 1
        # head가 끝까지 반복
        while head:
            # 홀수 순번일 경우 새로운 노드를 생성하여 odd에 추가
            if count % 2 == 1:
                odd.next = ListNode(head.val)
                odd = odd.next
            # 짝수 순번일 경우 새로운 노드를 생성하여 even에 추가
            else:
                even.next = ListNode(head.val)
                even = even.next
            head = head.next
            count += 1
        # 홀수의 끝에 짝수의 시작점 연결(짝수의 시작점이 0이기에 next를 통해 올바른 값이 넘어갈 수 있도록 추가)
        odd.next = dummy.next
        # 정답 연결리스트의 시작점이 0 이기에 올바른 값이 반환될 수 있도록 next한 값을 반환
        return result.next