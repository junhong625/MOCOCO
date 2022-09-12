class MyCircularDeque(object):  # 52/ms, 14.2mb

    def __init__(self, k):
        """
        :type k: int
        """
        self.leng = k
        self.d = collections.deque()
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.d) == self.leng:
            return False
        else :
            self.d.appendleft(value)
            return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.d) == self.leng:
            return False
        else :
            self.d.append(value)
            return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.d:
            self.d.popleft()
            return True
        else :
            return False
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.d:
            self.d.pop()
            return True
        else :
            return False
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.d:
            return(self.d[0])
        else:
            return (-1)
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.d:
            return(self.d[-1])
        else:
            return (-1)
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.d:
            return False
        else:
            return True
        

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.d) == self.leng:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()