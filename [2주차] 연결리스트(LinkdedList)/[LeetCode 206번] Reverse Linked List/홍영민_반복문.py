# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # 분명히 맞는거 같은데 시간 오바가 뜨는건지 아니면 이게 잘못되어 있는 건지
        # result = ListNode(0)
        # if not head:
        #     return head
        # while head:
        #     try:
        #         tmp = head.next
        #         result.next = head.val
        #         head = head.next
        #     except:
        #         result.val = head.val
        #         return result
        # return result

        # 이해는 한 코드
        prev = None
        cur = head
        while cur :
            tmp_next = cur.next # 우선 한단계 미룬것을 저장
            cur.next = prev # 이전 역순을 뒤에 더해준다
            prev = cur # 역순을 다시 저장
            cur = tmp_next # 한단계 미룬걸 다시 소환해서 루프로
        return prev
