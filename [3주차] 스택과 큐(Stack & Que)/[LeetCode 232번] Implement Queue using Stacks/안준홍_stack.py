# extand를 이용한 빠른 코드
class MyQueue(object):

    def __init__(self):
        self.que = []

    def push(self, x): # dummy를 이용해 먼저 들어온 값을 우측으로 이동 
        """
        :type x: int
        :rtype: None
        """
        dummy = [] 
        dummy.append(x)
        dummy.extend(self.que)
        self.que = dummy
        
    def pop(self): # popleft의 역할(push를 이용해 먼저 들어온 값이 끝에 있기에 pop을 이용)
        """
        :rtype: int
        """
        return self.que.pop()

    def peek(self): # 삭제기능이 없는 popleft의 역할
        """
        :rtype: int
        """
        return self.que[-1]

    def empty(self): # not을 통해 없을 경우 True, 있을 경우 False를 반환
        """
        :rtype: bool
        """
        return not self.que


# extand를 사용하지 않고 pop만을 이용한 코드

class MyQueue(object):

    def __init__(self):
        self.que = []

    def push(self, x): # 정상적으로 추가
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)
        
    def pop(self): # dummy를 이용해 뒤집은 후에 pop을 이용하여 처음으로 들어온 값을 빼낸다. 이후 다시 뒤집어 self.que에 저장
        """
        :rtype: int
        """
        dummy = []
        for _ in range(len(self.que)):
            dummy.append(self.que.pop())
        p = dummy.pop()
        for _ in range(len(dummy)):
            self.que.append(dummy.pop())
        return p

    def peek(self): # pop과 마찬가지로 뒤집은 후 pop이 아닌 인덱스 주소를 이용하여 해당 값을 가져오고 이후 다시 뒤집어 self.que에 저장
        """
        :rtype: int
        """
        print(self.que)
        dummy = []
        for _ in range(len(self.que)):
            dummy.append(self.que.pop())
        print(dummy)
        p = dummy[-1]
        for _ in range(len(dummy)):
            self.que.append(dummy.pop())
        print(self.que)
        return p

    def empty(self): # not을 통해 없을 경우 True, 있을 경우 False를 반환
        """
        :rtype: bool
        """
        return not self.que