class Node: # 일반적인 연결리스트와 다르게 뒤로 이동하는 포인터 추가
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next 
        self.prev = prev

class MyCircularDeque(object):

    def __init__(self, k): # 생성자 메서드
        """
        :type k: int
        """
        self.maxlen = k # 최대 길이
        self.head = self.tail = Node() # 새 연결리스트 생성
        self.cnt = 0 # 연결리스트 길이
        
    def insertFront(self, value): # appendleft의 역할
        """
        :type value: int
        :rtype: bool
        """
        if self.cnt == self.maxlen: # 가득 찼을 경우
            return False
        elif self.cnt == 0: # 연결리스트의 값이 없을 경우
            self.head.val = value
        else: # 연결리스트의 값이 있고 가득 차 있지 않은 경우
            head = Node(value, next=self.head)
            self.head.prev = head
            self.head = head
        self.cnt += 1
        return True

    def insertLast(self, value): # append의 역할
        """
        :type value: int
        :rtype: bool
        """
        if self.cnt == self.maxlen: # 가득 찼을 경우
            return False
        elif self.cnt == 0: # 연결리스트의 값이 없을 경우
            self.tail.val = value
        else: # 연결리스트의 값이 있고 가득 차 있지 않은 경우
            self.tail.next = Node(value, prev=self.tail)
            self.tail = self.tail.next
        self.cnt += 1
        
        return True
    
    def deleteFront(self): # popleft의 역할
        """
        :rtype: bool
        """
        if self.cnt > 1: # 연결리스트의 노드 개수가 2개 이상일 경우
            self.head = self.head.next
            self.cnt -= 1
            return True
        elif self.cnt == 1: # 연결리스트의 노드 개수가 1개인 경우 -> 연결리스트 초기화
            self.head = self.tail = Node()
            self.cnt = 0
            return True
        else: # 연결리스트의 값이 없을 경우
            return False
        

    def deleteLast(self): # popleft의 역할
        """
        :rtype: bool
        """
        if self.cnt > 1: # 연결리스트의 노드 개수가 2개 이상일 경우
            self.tail = self.tail.prev
            self.cnt -= 1
            return True
        elif self.cnt == 1: # 연결리스트의 노드 개수가 1개인 경우 -> 연결리스트 초기화
            self.head = self.tail = Node()
            self.cnt = 0
            return True
        else: # 연결리스트의 값이 없을 경우
            return False

    def getFront(self): # 첫번째 값 출력
        """
        :rtype: int
        """
        if self.cnt == 0:
            return -1
        return self.head.val

    def getRear(self): # 마지막 값 출력
        """
        :rtype: int
        """
        if self.cnt == 0:
            return -1
        return self.tail.val

    def isEmpty(self): # 비어있을 경우
        """
        :rtype: bool
        """
        return self.cnt == 0

    def isFull(self): # 가득 차 있을 경우
        """
        :rtype: bool
        """
        return self.cnt == self.maxlen 