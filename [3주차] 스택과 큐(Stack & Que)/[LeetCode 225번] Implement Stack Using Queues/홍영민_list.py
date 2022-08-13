class MyStack(object):

    def __init__(self):
        self.len = 0
        self.stack = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.len += 1
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        a = self.stack[self.len-1]
        self.stack = self.stack[:-1]
        self.len -= 1
        return a
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.len-1]

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack == []:
            return True
        else:
            return False
# len 변수를 활용해서 마지막에 있는 원소를 쉽게 불러오거나 뺄수 있게 되었다


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()