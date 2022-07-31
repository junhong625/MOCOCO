# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        palindrome_list = deque()
        
        # head에 값이 없을 때까지 반복
        while head is not None:
            # 현재 head의 값을 list에 추가
            palindrome_list.append(head.val)
            # head.next가 가리키는 다음 주소로 이동
            head = head.next
        
        while len(palindrome_list) > 1:
            # 일반적인 list를 사용하여 pop(0)으로 첫번째 값을 빼낼 시에는 모든 값이 한 칸씩 Shifting되기에 시간 복잡도 O(n)이 발생합니다.
            # 하지만 deque를 이용한 popleft()를 함으로써 Shifting이 되지 않기에 시간 복잡도가 O(n)보다 낮습니다.
            if palindrome_list.popleft() != palindrome_list.pop():
                return False
        return True
        