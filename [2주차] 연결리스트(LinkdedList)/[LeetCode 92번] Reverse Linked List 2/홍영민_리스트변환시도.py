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

        # (1,2)일 경우에 맞지 않다
        # root = head
        # for _ in range(0,left-1):
        #     head = head.next
        # n = left
        # while n < right:
        #     n += 2
        #     rev = head.next.next
        #     head.val, rev.val = rev.val, head.val
        #     head = head.next
        # return root
        
        #정답
        # 예외처리
        if not head or left == right:
            return head
        
        root = start = ListNode(0)
        root.next = head
        for _ in range(0,left-1):
            start = start.next
        end = start.next
        
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
    
    # 리스트로 변환하고 다시 역 변환시도했으나 계속 한가지 안되는게 발생. 죄송합니다 요번주 시간 없다고 너무 대충하네요
        a = []
        # if not head or left == right:
        #     return head
        
        # while head != None:
        #     a.append(head.val)
        #     head = head.next
        # left -= 1
        # right -= 1
        # if right-left == 1:
        #     a[left], a[right] = a[right], a[left]
        # if (right-left-1) % 2 == 0:
        #     for i in range(right-left-1):
        #         a[left + i], a[right-i] = a[right-i], a[left-i]

        # else: 
        #     for i in range(right-left-1):
        #         a[left + i], a[right-i] = a[right-i], a[left-i]
            
        # result = root = ListNode(0)

        # for i,num in enumerate(a):
        #     if i == 0 :
        #         result.val = num
        #     else :
        #         node = result
        #         while node.next != None:
        #             node = node.next
        #         node.next = ListNode(num)
        # return result