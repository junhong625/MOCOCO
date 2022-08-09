# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        up = 0
        head = ListNode(0)
        ans = head
        
        while up or l1 or l2:
            
            temp = up
            
            if l1 :
                temp += l1.val
                l1 = l1.next
            if l2 :
                temp += l2.val
                l2 = l2.next
            
            if temp >= 10 : #준홍갓갓
                up = 1
            else :
                up = 0
            
            head.next = ListNode(temp % 10)
            head = head.next
            
        return ans.next #55ms / 13.2mb