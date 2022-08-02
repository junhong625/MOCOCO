# 1. 초기에 생각했던 풀이코드 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rev = None
        node = head
        while node:
            rev = node
            node.next = rev
            node = node.next
        return rev

## 처음에 생각했던 방법은 rev에 node의 현재값을 집어 넣은 후 그 node의 다음 값을 rev로 설정하면
## 역순으로 연결리스트를 생성할 수 있지 않을까 생각했다. 
## 하지만 node.next가 rev로 바뀌면서 계속 현재 값을 가리키는 무한루프를 돌게 됐고 이를 해결할 수 있는 방법으로 
## node.next를 따로 변수에 미리 저장해주고 node의 다음 포인터를 rev로 설정한 후에 rev에 node를 할당하는 것이었다.

# 2. 해결 코드
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rev = None
        node = head
        while node:
            # node의 next 값을 미리 저장
            # 미리 저장해두지 않으면 아래에서 실행될 rev = node 코드로 인해 node.next가 변경이 되어버리기 때문
            next = node.next
            # 역순을 위해 node의 다음 포인터를 rev로 저장 
            # 이 코드를 반복하게 되면 ex) 5->4->3->2->1->None 이와 같이 역순으로 포인터가 저장이 됨
            node.next = rev
            # 아래 두 코드를 통해 rev는 항상 node 이전 포인트의 값을 가지게 된다.
            rev = node
            node = next
            # 아래의 코드는 전체적인 코드를 간단하게 만든 코드
            # rev, rev.next, node = node, rev, node.next 
        return rev