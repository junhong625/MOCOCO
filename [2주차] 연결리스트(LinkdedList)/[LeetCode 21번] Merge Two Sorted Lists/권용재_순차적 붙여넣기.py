class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        #빈 연결리스트 생성 - 결과를 넣을 것임
        result = ListNode()
        #현재의 노드
        current = result
        # 연결리스트를 다 순회할 때 까지 while
        while list1 and list2:
            #만약 list1의 현재 노드값이 list2의 노드값보다 크다면 list2를 current에 추가
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            # 그게 아니라면 list1을 current에 추가
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return result.next