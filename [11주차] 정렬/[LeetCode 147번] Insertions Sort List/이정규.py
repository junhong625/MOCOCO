# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        bigyo = meori = ListNode(0)
        
        while head:
            
            while bigyo.next and bigyo.next.val < head.val:
                
                bigyo = bigyo.next
            
            bigyo.next, head.next, head = head, bigyo.next, head.next
            
            if head and head.val < bigyo.val:
                
                bigyo = meori
        
        return meori.next