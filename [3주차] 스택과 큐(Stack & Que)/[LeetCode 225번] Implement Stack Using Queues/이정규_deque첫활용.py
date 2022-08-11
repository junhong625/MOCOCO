class MyStack(object):

    def __init__(self):
        self.q = collections.deque() # 데크가 짱이얌
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        # push된 값이 top에 있어야 하는데, 
        # queue에서 값이 나오는 곳은 맨 앞이므로
        
        self.q.rotate(1 - len(self.q)) # len(self.q) - 1 만큼 앞으로 보내기

    def pop(self):
        """
        :rtype: int
        """
        return self.q.popleft() # 삭제연산 이뤄지는 곳에서 삭제!
        

    def top(self):
        """
        :rtype: int
        """
        return self.q[0] # 삭제연산 이뤄지는 곳 위치!
        

    def empty(self):
        """
        :rtype: bool
        """
        
        return len(self.q) == 0 # 넌 길이가 몇이니?
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()