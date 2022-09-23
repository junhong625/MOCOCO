class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        node = collections.defaultdict(list)
        cir = []
        for i in range(n):
            cir.append(i)
        
        for unit in edges:
            node[unit[0]].append(unit[1])
            node[unit[1]].append(unit[0])
        
        cnt = n
        stack = collections.deque([])
        while cnt >= 2:
            if stack:
                while stack:
                    a, b = stack.pop()
                    node[a].remove(b)
                    cir.remove(b)
                    
            for idx in cir:
                if len(node[idx]) == 1:
                    stack.append([node[idx].pop(), idx])
                    cnt -= 1
            
        res = set()
        for unit in stack:
            res.add(unit[0])
        
        if res:
            return list(res)
        else:
            return [0]                  # 마지막 케이스(20000개짜리) 에서 타임에러남 ㅠㅠ