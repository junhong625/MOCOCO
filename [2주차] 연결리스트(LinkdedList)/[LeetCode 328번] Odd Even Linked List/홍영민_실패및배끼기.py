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
        n = 1
        root1 = odd = ListNode(0)
        root2 = even = ListNode(0)
        while head:
            if n % 2 == 1:
                odd.next = head
                head = head.next
                odd = odd.next
                n += 1
            else:
                even.next = head
                even = even.next
                head = head.next
                n += 1
        odd.val(root2.next) 
        '''문제는 두가지  
        1. 마지막 odd 값은 현재 none이기 때문에 listnode의 형식이 아니라 뒤에 무엇을 붙일 수 없다는 점
        2. even 처리가 마지막이 되지 않는다면 (길이가 짝수가 아니면) 뒤에 홀수가 하나 붙어버린다는 점
        그러므로 실패작이다   '''
        return odd

    def oddEvenList(self,head):
        if head is None:
            return head

        odd = head
        even_head = even = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head

        ## 이 문제가 제일 이해가 안되네요 자료구조가 이해가 안됨
        #넣는 방법은 이해하기 쉬운데 왜 저렇게 넣는지, even_head는 왜 바뀌어 있는지 이해가 안됨