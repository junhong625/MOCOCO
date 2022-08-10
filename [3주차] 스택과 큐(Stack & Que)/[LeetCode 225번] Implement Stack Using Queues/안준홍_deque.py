class MyStack(object):
    from collections import deque # que를 사용

    def __init__(self): # stack을 que로 저장
        self.stack = deque() 

    def push(self, x): # 끝에 추가한 후 추가된 인덱스 기준으로 뒤집기
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        for _ in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())

    def pop(self): # push를 하며 뒤집었기에 popleft()로 빼낸 값이 마지막으로 입력된 값
        """
        :rtype: int
        """
        return self.stack.popleft()

    def top(self): # 마찬가지로 제일 처음 값이 마지막으로 입력된 값
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self): # not을 통해 없을 경우 True, 있을 경우 False를 반환
        """
        :rtype: bool
        """
        return not self.stack
        