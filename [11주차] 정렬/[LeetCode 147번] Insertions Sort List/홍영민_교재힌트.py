# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        go = head
        result = compare = ListNode(None)
        if not head:
            return head
        while go:
            print(go.val)
            while compare:
                if compare.next and compare.next.val < go.val:
                    compare = compare.next
                else:
                    compare.next = ListNode(go.val,next=compare.next)
                    break
            compare = result
            go = go.next
        return result.next
    # 원래 삽입정렬은 오른쪽에서 왼쪽으로 진행한다
    # 다만, 연결리스트는 불가능이다
    # 초과하는 경우에만 제일 앞으로 돌아가도록 바꿔주었다?? 이 초기값으로 돌아가는 조건이 이해가 잘 안됩니다
    def insertionSortlist(self, head):
        cur = parent=ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
        if head and cur.val > head.val:
            cur = parent
        return parent.next