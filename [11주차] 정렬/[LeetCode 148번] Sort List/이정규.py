# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        
        temp.sort()
        
        ans = ListNode()
        head = ans
        for unit in temp:
            ans.next = ListNode()
            ans = ans.next
            ans.val = unit
        
        return head.next
            