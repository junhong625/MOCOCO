class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
#         if head == 0:
#             return False
        
#         q = []
#         node = head
        
#         while node is not None:
#             q.append(node.val)
#             node = node.next
        
#         while len(q) > 1:
#             if q.pop(0) != q.pop():
#                 return False
#         return True
        d = collections.deque()
        
        node = head
        while node is not None:
            d.append(node.val)
            node = node.next
        while len(d) > 1:
            if d.popleft() != d.pop():
                return False
        return True
    