class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        current = result        #현재 노드 0에서 시작
        
        
        #올림 하려고 만든 변수
        carry = 0
        #l1과 l2를 순회할 때 까지
        while l1 and l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            carry, val = divmod(sum+carry,10)  #올림 수 까지 더해서 몫과 나머지
            current.next = ListNode(val) 
            current = current.next 
        return result.next

## ???? 이거 근데 왜 연결리스트 노드 수가 같아야지만 계산이 되는거징..? 흑흑