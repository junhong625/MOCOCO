# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  
        self.val = val
        self.next = next
        

        ### 이게 왜 안 되는지 여러분들께 여쭤보고 싶습니다... ###


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def fn(x):
            while True:
                try: 
                    x.next = x.next.next 
                    x = x.next
                except:
                    break
            return x
        
        odd = head
        even = head.next
        even_head = head.next

        odd, even = fn(odd), fn(even)
        odd.next = even_head

        return head