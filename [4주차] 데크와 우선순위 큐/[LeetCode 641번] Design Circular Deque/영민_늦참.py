class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k = k
        self.len = 0
        self.head.right = self.tail
        self.tail.left = self.head
        
    def _add(self, main, new):
        n = main.right
        main.right = new
        new.left, new.right = main, n
        n.left = new
        
    def _del(self, main):
        n = main.right.right
        main.right = n
        n.left = main

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.k == self.len:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.k == self.len:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True
        
    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self):
        """
        :rtype: int
        """
        return self.head.right.val if self.len else -1

    def getRear(self):
        """
        :rtype: int
        """
        return self.tail.left.val if self.len else -1
    

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.len == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.len == self.k
