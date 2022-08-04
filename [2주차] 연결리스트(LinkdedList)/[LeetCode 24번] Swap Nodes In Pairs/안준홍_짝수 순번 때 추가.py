# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 순번을 계산하는 카운트
        count = 1
        # 시작점의 역할을 할 result, 연결리스트 후미 역할을 할 dummy
        result = dummy = ListNode()
        # 홀수 순번을 저장해둘 변수
        odd_node = None
        # head의 끝까지 반복
        while head:
            # 순번이 홀수일 경우 odd_node에 head.val을 집어넣어 새로운 노드를 생성해서 할당
            if count % 2 == 1:
                odd_node = ListNode(head.val)
            # 순번이 짝수일 경우 val에 head.val과 다음포인터(next)에 odd_node를 넣어 생성한 노드를 미리 생성해둔 연결리스트 후미의 다음포인터(next)로 할당
            # 할당 후 odd_node는 초기화
            else:
                dummy.next = ListNode(head.val, odd_node)
                dummy = dummy.next.next
                odd_node = None
            # 순번을 계산하기 위해 count+=1 해주고 head를 다음 포인터로 이동
            count += 1
            head = head.next
        # odd_node가 남아있다는 것은 head의 길이가 홀수라서 마지막 노드가 추가되지 않았다는 의미
        # 그렇기에 odd_node가 남아있다면 연결리스트 후미의 다음 포인터로 할당
        if odd_node:
            dummy.next = odd_node
            
        # result는 새로 생성한 연결리스트로 시작점이 0이기에 next를 해야 올바른 정답 출력
        return result.next 