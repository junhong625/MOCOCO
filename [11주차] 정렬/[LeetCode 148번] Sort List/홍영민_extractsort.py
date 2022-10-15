# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head:
            return head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        stack.sort()
        root = result = ListNode()
        print(result)
        for i in range(len(stack)):
            result.val = stack[i]
            if i != len(stack)-1:
                result.next = ListNode()
            result = result.next
        return root
            
