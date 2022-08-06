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
        # 2번에서 우리는 얕은 복사로 정답을 미리 저장해 둘 수 있다는 것을 배웠다
        root = head
        #이를 활용해서 head만 변화시키면 된다
        while head and head.next:
            # 갯수가 짝수가 아닐 경우 next값이 none이므로 오류가 발생하므로 둘다 만족해야 한다
            head.val, head.next.val = head.next.val, head.val # 바로 바꿈
            head = head.next.next  # 바꾸고 2개 건너뛰기
        return root

        ## 추가로 재귀함수를 활용한 답안
        # def swapPairs(self,head):
        #     if head and head.next:
        #         p = head.next
        #         #앞으로 두개 보낸거 재귀
        #         head.next = (self.swapPairs(p.next))
        #         p.next = head
        #         return p
        #     return head