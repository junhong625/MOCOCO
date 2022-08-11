# Linked List를 이용한 코드

class Node: # Linked List의 Node 생성 클래스
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyCircularQueue(object):

    def __init__(self, k): # 생성자 메서드
        """
        :type k: int
        """
        self.max_len = k # 최대 길이 생성
        self.tail = self.head = Node() # 연결리스트의 생성(value를 주지 않고 Node를 생성했기에 실질적으로 해당 노드의 next가 헤드의 역할) 
        self.cnt = 0 # 연결리스트의 길이

    def enQueue(self, value): # 연결리스트에 값 추가
        """
        :type value: int
        :rtype: bool
        """
        if self.cnt == self.max_len: # 연결리스트의 길이가 최대값이 경우 아무 작업도 수행하지 않음
            return 
        self.tail.next = Node(value) # 테일을 생성하여 연결리스트의 꼬리로 설정 
        self.tail = self.tail.next # 다음 노드로 이동
        self.cnt += 1 # 길이 +1
        
        return True
    
    def deQueue(self): # popleft의 역할 즉, 연결리스트의 헤드 삭제
        """
        :rtype: bool
        """
        if not self.head.next: # 연결리스트의 헤드가 비어있을 경우
            return
        self.head = self.head.next # 헤드를 다음 노드로 변경
        self.cnt -= 1 # 길이 -1
        
        return True

    def Front(self): # 리스트 제일 앞쪽의 값
        """
        :rtype: int
        """
        if self.head.next: # 헤드가 존재할 경우
            return self.head.next.val # 헤드의 값 반환
        return -1

    def Rear(self): # 리스트 제일 뒤쪽의 값
        """
        :rtype: int
        """
        if self.head.next: #헤드가 존재할 경우
            return self.tail.val # 테일의 값 반환
        return -1

    def isEmpty(self): # 비어 있는지 체크
        """
        :rtype: bool
        """
        return not self.head.next # not을 통해 존재할 경우 False를 반환, 존재하지 않을 경우 True를 반환

    def isFull(self): # 가득 찼는지 체크
        """
        :rtype: bool
        """
        return self.cnt == self.max_len # 현재 연결리스트 길이와 최대 길이 비교한 bool값 반환

# stack구조를 이용한 코드

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = []
        self.max_len = k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.q) == self.max_len:
            return False
        self.q.append(value)
        return True
    
    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.q:
            return
        dummy = []
        for _ in range(len(self.q)):
            dummy.append(self.q.pop())
        p = dummy.pop()
        for _ in range(len(dummy)):
            self.q.append(dummy.pop())
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q[0]
        return -1

    def Rear(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q[-1]
        return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return not self.q

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.q) == self.max_len


# 왜 큐를 쓰는데 더 느리지...?
from collections import deque
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = deque()
        self.max_len = k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.q) == self.max_len:
            return False
        self.q.append(value)
        
        return True
    
    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.q:
            return
        self.q.popleft()
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q[0]
        return -1

    def Rear(self):
        """
        :rtype: int
        """
        print(self.q)
        if self.q:
            return self.q[-1]
        return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return not self.q

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.q) == self.max_len