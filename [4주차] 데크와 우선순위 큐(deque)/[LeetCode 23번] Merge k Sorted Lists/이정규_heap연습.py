class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):     # 225ms, 22.4mb
    def mergeKLists(self, lists):
        import heapq
        
        temp = []
        for nodes in lists:
            while nodes:
                heappush(temp, nodes.val)
                nodes = nodes.next
        
        root = end = ListNode()
        while temp:
            end.next = ListNode(heappop(temp))
            end = end.next
            
        return root.next