# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from matplotlib.container import Container


class Solution:
    class Container:
        def __init__(self, node):
            self.node = node
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode(None)
        root.next = head
        for _ in range(left-1):
            start = start.next
        end = start.next
        
        idx = 0
        while True:
            temp = ListNode(start.val)


            

