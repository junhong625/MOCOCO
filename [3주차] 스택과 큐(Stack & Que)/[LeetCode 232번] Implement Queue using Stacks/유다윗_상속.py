import copy
class MyStack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)
    
    def top(self):
        return self.s[-1]
    
    def pop(self):
        return self.s.pop()
    
    def empty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

class MyQueue(MyStack):
    def __init__(self):
        super().__init__()

    def peek(self):
        top = 0
        for t in range(2):
            temp = []
            for i in range(len(self.s)):
                temp.append(super().pop())
            self.s = copy.deepcopy(temp)
            if t == 0:
                top = self.top()
        return top
    
    def pop(self):
        popped = 0
        for t in range(2):
            temp = []
            for i in range(len(self.s)):
                temp.append(super().pop())
            self.s = copy.deepcopy(temp)
            if t == 0:
                popped = super().pop()
        return popped

# a = MyQueue()
# a.push(1)
# a.push(2)
# a.push(3)
# print(a.pop())
# print(a.peek())
# print(a.s)
# print(a.pop())
# print(a.s)