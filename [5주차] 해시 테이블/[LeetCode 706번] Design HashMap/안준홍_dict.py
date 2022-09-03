class MyHashMap(object):

    def __init__(self):
        self.hashmap = dict()        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashmap[key] = value
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            return self.hashmap[key]
        else:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashmap:
            del self.hashmap[key]