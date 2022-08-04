# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # return할 ListNode인 node 정의
        head = ListNode(0)
        node = head

        # sum_result: input 리스트들의 자릿수를 더한 값을 할당할 변수
        sum_result = 0
        # carry_save: 자릿수의 합이 10이상일 경우(자리올림 수) 1, 아닐 경우 0을 가질 변수
        carry_save = 0
        
        while True:
            # 두 리스트 모두 더 이상 원소가 없을 경우(즉, 끝에 도달했을 때) break
            if not(l1 or l2):
                # 만약 자리올림 수가 있을 경우 마지막 노드 추가(val은 1)
                if carry_save == 1:
                    node.next = ListNode(1)
                    break
                else:
                    break
            # l1 리스트에 원소가 있을 경우 val값을 sum_result에 더한다.
            if l1:
                sum_result += l1.val
                l1 = l1.next
            # l2 리스트에 원소가 있을 경우 val값을 sum_result에 더한다.
            if l2:
                sum_result += l2.val
                l2 = l2.next
            
            if sum_result >= 10:
                # 자리올림 수가 존재할 경우
                if carry_save:
                    # sum_result의 일의자리수와 자리올림 수 1을 더했을 때 10이 안 될 경우
                    if (sum_result - 10 + 1) != 10:
                        # node.next 추가
                        node.next = ListNode(sum_result - 10 + 1)
                        node = node.next
                        # sum_result가 10 이상이기 때문에 carry_save에 1 할당
                        carry_save = 1
                    else:
                        # sum_result의 일의자리수와 자리올림 수 1을 더했을 때 10이 되었기 때문에
                        # node.next의 val은 0
                        node.next = ListNode(0)
                        node = node.next
                        # sum_result가 10 이상이고, sum_result의 일의자리수와 자리올림 수 1을 더했을 때 
                        # 또 다시 자리올림 수가 발생했기 때문에 carry_save에 2 할당
                        carry_save = 2
                # 자리올림 수가 존재하지 않을 경우
                else:
                    node.next = ListNode(sum_result - 10)
                    node = node.next
                    carry_save = 1
            else:
                if carry_save:
                    if (sum_result + 1) != 10:
                        node.next = ListNode(sum_result + 1)
                        node = node.next
                        carry_save = 0
                    else:
                        node.next = ListNode(0)
                        node = node.next
                        carry_save = 1
                else:
                    node.next = ListNode(sum_result)
                    node = node.next
                    carry_save = 0
                
            # sum_result 초기화
            sum_result = 0
        
        node = head.next
        return node