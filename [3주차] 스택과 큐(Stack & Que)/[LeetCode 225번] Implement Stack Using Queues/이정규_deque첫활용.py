class MyStack(object):

    def __init__(self):
        self.self_stack = collections.deque() # 데크가 짱이얌
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.self_stack.append(x)
        # push된 값이 top에 있어야 하는데, 
        # queue에서 값이 나오는 곳은 맨 앞이므로
        
        self.self_stack.rotate(1 - len(self.self_stack)) # len(self.self_stack) - 1 만큼 앞으로 보내기

    def pop(self):
        """
        :rtype: int
        """
        return self.self_stack.popleft() # 삭제연산 이뤄지는 곳에서 삭제!
        

    def top(self):
        """
        :rtype: int
        """
        return self.self_stack[0] # 삭제연산 이뤄지는 곳 위치!
        

    def empty(self):
        """
        :rtype: bool
        """
        
        return len(self.self_stack) == 0 # 넌 길이가 몇이니?
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
