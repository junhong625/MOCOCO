# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        before = None
        
        while head :
            head.next, after = before, head.next
            before, head = head, after
        
    
        return before # 29ms, 15.3mb