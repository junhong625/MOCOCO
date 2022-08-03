# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head에 요소가 없을 경우 none 출력
        if not head:
            return None
        
        new_list = head
        prev = None
        
        while True:
            next_element = new_list.next
            new_list.next = prev
            prev = new_list
            new_list = next_element
            
            # head의 끝에 도달했을 때 break
            if not new_list:
                break

        return prev
            