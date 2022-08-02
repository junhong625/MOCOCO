# 1. 처음으로 생각했던 풀이

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, a, b):
        head = result = ListNode()
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        while a and b:
            if a.val < b.val:
                head.next = ListNode(a.val)
                # a, head = a.next, a
                head = ListNode(a.val)
                a = a.next
            else:
                head.next = ListNode(b.val)
                # a, head = a.next, a
                head = ListNode(b.val)
                b = b.next
        if a or b:
            head.next = a if a else b
            
        return result.next
## 변수를 생성하지 않고 바로 포인터를, 새로 만든 노드로 찍으면 가능할 줄 알았다.
## 하지만 head.next와 head에 들어간 노드의 id를 확인해본 결과 서로 다른 Node였다.
## 그렇기에 새로 생성한 연결 리스트가 값들이 이어지지 않고 끊어지던 것이었다.

# 2. 수정한 풀이
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, a, b):
        # 노드를 연결할 head와 결과를 반환할 result, 두 연결리스트 생성(같은 주소를 가리키고 있음)
        head = result = ListNode()
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # a나 b의 데이터가 None이 될 때 까지 반복
        while a and b:
            # a의 값이 b보다 작을 경우
            if a.val < b.val:
                # 1. 다음 노드 dummy를 생성
                # 2. head의 포인터 dummy로 설정
                # 3. head를 포인터로 이동
                dummy = ListNode(a.val)
                head.next = dummy
                head = head.next
                # 위 세 라인의 코드를 아래와 같은 한 줄 코드로 대체 할 수 있음
                # a, head = a.next, a 
                # a를 다음 포인터로 이동
                a = a.next
            else:
                dummy = ListNode(b.val)
                head.next = dummy
                # head = head.next와 같은 결과를 가져오는 코드
                head = dummy
                # b, head = a.next, b
                b = b.next
        
        # 한쪽의 값이 None이 되면 아직 데이터가 남아 있는 값의 나머지들을 현재 값의 다음 포인터로 지정
        if a or b:
            head.next = a if a else b
        
        # 첫 시작 값이 0이기 때문에 그 다음 값 부터 출력
        return result.next