# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 리스트 1과 2 모두 빈 경우 None 리턴
        if not(list1 or list2):
            return None
        
        
        ## val값만 추출해서 두 리스트 합치기 ##
        node_vals = []
        # list1
        if list1:
            while True:
                node_vals.append(list1.val)
                list1 = list1.next
                if list1 == None:
                    break

        # list2
        if list2:
            while True:
                node_vals.append(list2.val)
                list2 = list2.next
                if list2 == None:
                    break
        

        ## 오름차순 정렬 ##
        node_vals.sort()

        ## 정렬된 새로운 node 만들기 ##
        head = ListNode(node_vals[0])
        
    
        ## 연결 리스트 새로 만들어서 출력하기 ##
        # value가 하나일 경우
        if len(node_vals) == 1:
            node = ListNode(node_vals[0])
            return node
        # value가 두 개 이상일 경우
        else:
            idx = 1
            node = head
            while True:
                node.next = ListNode(node_vals[idx])
                node = node.next
                idx += 1
                if idx == len(node_vals):
                    break
                    
            node = head
            return node

