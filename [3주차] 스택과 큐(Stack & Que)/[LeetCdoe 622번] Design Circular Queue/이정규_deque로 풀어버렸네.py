class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.cq = collections.deque()
        self.qlen = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.cq) == self.qlen:
            return False
        else:
            self.cq.append(value)
            return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.cq:
            self.cq.popleft()
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int
        """
        if self.cq:
            return(self.cq[0])
        else:
            return -1
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.cq:
            return(self.cq[-1])
        else:
            return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return False if self.cq else True

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.cq) == self.qlen:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()