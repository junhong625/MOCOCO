# 간단하게 연결리스트의 모든 값들을 리스트에 집어 넣어 정렬 후 연결리스트로 생성

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 새로운 연결리스트 생성, result는 연결리스트의 헤드
        result = new_list = ListNode()
        # 연결리스트의 값들이 들어갈 변수
        values = []
        # 모든 연결리스트의 값들을 values에 추가
        for l_list in lists:
            while l_list:
                values.append(l_list.val)
                l_list = l_list.next
        # 오름차순으로 정렬
        values.sort()
        # values에서 하나씩 값을 꺼내 새로운 노드로 생성하여 이어주기
        for val in values:
            new_list.next = ListNode(val)
            new_list = new_list.next
        # result의 현재 값은 0이고 다음 포인터로 이동한 값을 반환해줘야 올바른 정답을 반환
        return result.next