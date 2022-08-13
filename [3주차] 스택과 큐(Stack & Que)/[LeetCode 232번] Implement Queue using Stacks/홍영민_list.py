class MyQueue(object):

    def __init__(self):
        self.queue = []
        self.output = []

    def push(self, x):
        self.queue.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        self.peek()
        return self.output.pop()
        """
        :rtype: int
        """
    
    # 마지막에 있는 아이템을 조회하기 위해선 전체를 따로 저장해 두는 것이 쉽다
    def peek(self):
        if not self.output:
            while self.queue:
                self.output.append(self.queue.pop())
        return self.output[-1]
        """
        :rtype: int
        """
        

    def empty(self):
        if self.queue == [] and self.output == []:
            return True
        else : 
            return False
        """
        :rtype: bool
        """
        
# output에 따로 input을 모두 저장해 두면 귀찮게 새로 불러오고 할 필요는 없다. 다만 이는 실제 queue 가 될수는 없다