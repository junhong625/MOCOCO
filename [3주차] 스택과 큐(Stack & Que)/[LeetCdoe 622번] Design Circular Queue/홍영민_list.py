## 헤맨점은 포인트가 최대 길이를 초과할 경우 나눠주는 부분을 작성했어야 한다는 점
## 두번째로는 if a: 를 작성할때 0이 들어가게되면 none이랑 동급으로 취급해서 모든 조건에 == none을 적어줬어야 했다는 점
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.circle = [None]*k
        self.len = 0
        self.front = 0
        self.k = k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        
        if self.circle[self.len]:
            return False
        else:
            self.circle[self.len] = value
            self.len = (self.len +1) % self.k
            return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.circle[self.front] == None:
            k = self.circle[self.front]
            self.circle[self.front] = None
            self.front = (self.front+1) % self.k
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int
        """
        front = self.circle[self.front]
        if front == None:
            return -1
        else:
            return front

    def Rear(self):
        """
        :rtype: int
        """
        rear = self.circle[self.len - 1]
        if rear == None:
            return -1
        else:
            return rear

    def isEmpty(self):
        """
        :rtype: bool
        """
        for i in self.circle:
            if i:
                return False
        else:
            return True

    def isFull(self):
        """
        :rtype: bool
        """
        for i in self.circle:
            if i == None:
                return False
        else:
            return True

