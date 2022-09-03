class MyHashMap(object):

    def __init__(self):
        self.visit = [False] * 10**7
        self.val = [None] * 10**7

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.visit[key] = True
        self.val[key] = value
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.visit[key] == True:
            return self.val[key]
        else:
            return -1
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.visit[key] = False
        self.val[key] = None        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)