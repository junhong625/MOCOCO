class Stack:
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

class MyQueue(Stack):
    def __init__(self):
        super().__init__()
        # 두 번째 stack
        self.s2 = []

    # def push(self, x):
    #     super().push(x)

    def peek(self):
        for i in range(len(self.s)):
            self


a = MyQueue()
a.push(1)
print(a.s)