class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        current = head
        
        while current and current.next:
            # 페어로 앞뒤 바꾸기
            current.val,current.next.val = current.next.val,current.val #이거 두줄로 표현하면 값이 달라지더라요
                      
            current = current.next.next
        return head
            